import os
import psycopg

conn = psycopg.connect(
    host=os.getenv("PGHOST", "localhost"),
    port=os.getenv("PGPORT", "5432"),
    dbname=os.getenv("PGDATABASE", "SupermercadoDB"),
    user=os.getenv("PGUSER", "postgres"),
    password=os.getenv("PGPASSWORD", "postgres"),
)

def escape_val(v):
    if v is None:
        return "null"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v).replace("'", "''")
    return f"'{s}'"

def fetch_rows(cur, sql, params=None):
    cur.execute(sql, params or ())
    cols = [d[0] for d in cur.description]
    return cols, cur.fetchall()

def format_relation(name, cols, rows):
    header = f"{name} = {{\n  " + ", ".join(cols)
    body = "\n".join("  " + ", ".join(escape_val(v) for v in r) for r in rows)
    return f"{header}\n{body}\n}}" if body else f"{header}\n}}"

with conn:
    with conn.cursor() as cur:
        # 1. Muestra base de incluir (25 filas) para garantizar integridad referencial
        inc_cols, inc_rows = fetch_rows(cur, """
            SELECT ticket, cod_barra
            FROM incluir
            ORDER BY ticket, cod_barra
            LIMIT 25
        """)
        inc_tickets = list(dict.fromkeys(r[0] for r in inc_rows))
        inc_cods = list(dict.fromkeys(r[1] for r in inc_rows))

        # 2. Productos (los de incluir + extra hasta completar 20)
        prod_cols, prod_rows = fetch_rows(cur, """
            (SELECT * FROM productos WHERE cod_barra = ANY(%s))
            UNION
            (SELECT * FROM productos ORDER BY cod_barra LIMIT 20)
            LIMIT 20
        """, (inc_cods or [""],))
        cods = [r[0] for r in prod_rows] or [""]

        # 3. Categorias asociadas a esos productos
        cat_cols, cat_rows = fetch_rows(cur, """
            SELECT * FROM categoria
            WHERE cod_barra = ANY(%s)
            LIMIT 25
        """, (cods,))
        cat_ids = list(dict.fromkeys(r[1] for r in cat_rows)) or [""]

        # 4. Catalogo de categorias (las usadas + extra hasta completar 15)
        cat_cat_cols, cat_cat_rows = fetch_rows(cur, """
            (SELECT * FROM categoria_catalogo WHERE id_categoria = ANY(%s))
            UNION
            (SELECT * FROM categoria_catalogo ORDER BY id_categoria LIMIT 15)
            LIMIT 15
        """, (cat_ids,))

        # 5. Ventas (las de incluir + extra hasta completar 20)
        venta_cols, venta_rows = fetch_rows(cur, """
            (SELECT * FROM venta WHERE ticket = ANY(%s))
            UNION
            (SELECT * FROM venta ORDER BY ticket LIMIT 20)
            LIMIT 20
        """, (inc_tickets or [""],))
        tickets = [r[0] for r in venta_rows] or [""]

        # Re-filtrar incluir por los tickets y productos efectivamente exportados
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
print(f"Conteo -> categoria_catalogo: {len(cat_cat_rows)}, productos: {len(prod_rows)}, categoria: {len(cat_rows)}, venta: {len(venta_rows)}, incluir: {len(inc_rows)}")
