import os
import time
import psycopg

conn_info = (
    f"host=db dbname={os.environ['POSTGRES_DB']} "
    f"user={os.environ['POSTGRES_USER']} password={os.environ['POSTGRES_PASSWORD']}"
)

consultas = [
    {
        "pregunta": "1. Obtener nombre y precio de los productos con precio mayor a 500.",
        "algebra": "π nombre, precio (σ precio > 500 (productos))",
        "sql": "SELECT nombre, precio FROM productos WHERE precio > 500 ORDER BY precio DESC;"
    },
    {
        "pregunta": "2. Obtener el ticket, total y anio de las ventas realizadas en 2025 con total mayor a 2000.",
        "algebra": "π ticket, total, anio (σ anio = 2025 ∧ total > 2000 (venta))",
        "sql": "SELECT ticket, total, anio FROM venta WHERE anio = 2025 AND total > 2000 ORDER BY total DESC;"
    },
    {
        "pregunta": "3. Obtener las categorias catalogadas con nombre 'Bebidas' o 'Limpieza'.",
        "algebra": "π id_categoria, nombre (σ nombre = 'Bebidas' ∨ nombre = 'Limpieza' (categoria_catalogo))",
        "sql": "SELECT id_categoria, nombre FROM categoria_catalogo WHERE nombre IN ('Bebidas', 'Limpieza') ORDER BY id_categoria;"
    }
]

def formatear_valor_relax(val):
    if val is None:
        return "null"
    if isinstance(val, (int, float)):
        return str(val)
    texto = str(val).replace("'", "\\'")
    return f"'{texto}'"

conn = None
for intento in range(15):
    try:
        conn = psycopg.connect(conn_info)
        break
    except psycopg.OperationalError as e:
        print(f"Esperando a la base de datos (intento {intento + 1}/15): {e}")
        time.sleep(2)

if conn is None:
    raise RuntimeError("No fue posible conectar a la base de datos 'db' tras varios intentos.")

with conn:
    with conn.cursor() as cur:
        print("=" * 60)
        print("CONSULTAS PARTE 2")
        print("=" * 60)
        for c in consultas:
            print(f"\nPREGUNTA: {c['pregunta']}")
            print(f"ALGEBRA RELACIONAL:\n  {c['algebra']}")
            print(f"SQL:\n  {c['sql']}")
            cur.execute(c["sql"])
            cols = [desc[0] for desc in cur.description]
            rows = cur.fetchall()
            print("RESULTADO:")
            print("  " + " | ".join(cols))
            for r in rows:
                print("  " + " | ".join(str(x) for x in r))
            print("-" * 60)

        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
            ORDER BY table_name;
        """)
        tablas = [r[0] for r in cur.fetchall()]

        os.makedirs("/app/salida", exist_ok=True)
        ruta_relax = "/app/salida/grupo_relax_regenerado.txt"
        with open(ruta_relax, "w", encoding="utf-8") as f_out:
            f_out.write("group: SupermercadoNormalizado\n\n")
            for tabla in tablas:
                cur.execute(f'SELECT * FROM "{tabla}" LIMIT 50;')
                cols = [desc[0] for desc in cur.description]
                rows = cur.fetchall()
                f_out.write(f"{tabla} = {{\n")
                f_out.write("  " + ", ".join(cols) + "\n")
                for row in rows:
                    vals = ", ".join(formatear_valor_relax(v) for v in row)
                    f_out.write(f"  {vals}\n")
                f_out.write("}\n\n")

        print(f"\n[OK] Grupo RelaX regenerado en: {ruta_relax}")
