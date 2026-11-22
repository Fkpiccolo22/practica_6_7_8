import os
import psycopg

conn = psycopg.connect(
    host=os.getenv("PGHOST", "localhost"),
    port=os.getenv("PGPORT", "5432"),
    dbname=os.getenv("PGDATABASE", "SupermercadoDB"),
    user=os.getenv("PGUSER", "postgres"),
    password=os.getenv("PGPASSWORD", "postgres"),
)


def fmt_val(v):
    if v is None:
        return "null"
    if isinstance(v, (int, float)):
        return str(v)
    texto = str(v).replace("'", "''")
    return f"'{texto}'"


def fetch_rows(cur, sql, params=None):
    cur.execute(sql, params or ())
    cols = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return cols, rows


def format_relation(name, cols, rows):
    lines = [f"{name} = {{", "  " + ", ".join(cols)]
    for r in rows:
        lines.append("  " + ", ".join(fmt_val(v) for v in r))
    lines.append("}")
    return "\n".join(lines)


with conn:
    with conn.cursor() as cur:
        # 1. Catalogo de categorias
        cat_cat_cols, cat_cat_rows = fetch_rows(cur, """
            SELECT id_categoria, nombre
            FROM categoria_catalogo
            ORDER BY id_categoria
            LIMIT 20
        """)
        cat_ids = [r[0] for r in cat_cat_rows] or ["''"]

        # 2. Productos
        prod_cols, prod_rows = fetch_rows(cur, """
            SELECT cod_barra, nombre, marca, precio
            FROM productos
            ORDER BY cod_barra
            LIMIT 20
        """)
        cods = [r[0] for r in prod_rows] or ["''"]

        # 3. Relacion producto-categoria (respetando los ids exportados)
        cat_cols, cat_rows = fetch_rows(cur, """
            SELECT cod_barra, identificador
            FROM categoria
            WHERE cod_barra = ANY(%s) AND identificador = ANY(%s)
            LIMIT 25
        """, (cods, cat_ids))

        # 4. Ventas (ya normalizada, sin empleadoventas)
        venta_cols, venta_rows = fetch_rows(cur, """
            SELECT ticket, identificador_cliente, identificador_empleado, total, dia, mes, anio
            FROM venta
            ORDER BY ticket
            LIMIT 20
        """)
        tickets = [r[0] for r in venta_rows] or ["''"]

        # 5. Detalle incluir (respetando tickets y cod_barra exportados)
        inc_cols, inc_rows = fetch_rows(cur, """
            SELECT ticket, cod_barra
            FROM incluir
            WHERE ticket = ANY(%s) AND cod_barra = ANY(%s)
            LIMIT 25
        """, (tickets, cods))

blocks = [
    "group: SupermercadoNormalizado",
    format_relation("categoria_catalogo", cat_cat_cols, cat_cat_rows),
    format_relation("productos", prod_cols, prod_rows),
    format_relation("categoria", cat_cols, cat_rows),
    format_relation("venta", venta_cols, venta_rows),
    format_relation("incluir", inc_cols, inc_rows),
]

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grupo.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(blocks) + "\n")

print(f"Listo: se genero {out_path}")
