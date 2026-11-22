## Selección (σ) y Proyección (π)

### Consulta 1.1: Productos con precio mayor a 100
1. **Pregunta del dominio:** ¿Cuáles son el código de barras, nombre y precio de los productos cuyo precio es mayor a 100?
2. **Expresión en álgebra relacional:**
   `π cod_barra, nombre, precio (σ precio > 100 (productos))`
3. **Captura de RelaX (árbol y resultado):**
   <img width="648" height="540" alt="image" src="https://github.com/user-attachments/assets/69791e0a-527f-4285-86f2-7fc53248dab9" />

4. **SQL equivalente y comprobación:**
   ```sql
   SELECT cod_barra, nombre, precio
   FROM productos
   WHERE precio > 100;
   ```
   
   <img width="1006" height="729" alt="image" src="https://github.com/user-attachments/assets/34765cbb-8ebd-4441-8d60-7c83112e9a2d" />

### Consulta 1.2: Ventas de diciembre de 2025
1. **Pregunta del dominio:** ¿Cuáles son el ticket y el total de las ventas registradas en el mes 12 del año 2025?
2. **Expresión en álgebra relacional:**
   `π ticket, total (σ mes = 12 ∧ anio = 2025 (venta))`
3. **Captura de RelaX (árbol y resultado):**
   <img width="661" height="531" alt="image" src="https://github.com/user-attachments/assets/ff16a1e5-0ec8-4ab4-8efd-0fe485cffb68" />
   <img width="645" height="424" alt="image" src="https://github.com/user-attachments/assets/a2023fb4-1f1b-4505-accc-0c25147b3b16" />

4. **SQL equivalente y comprobación:**
   ```sql
   SELECT ticket, total
   FROM venta
   WHERE mes = 12 AND anio = 2025;

<img width="1005" height="725" alt="image" src="https://github.com/user-attachments/assets/91fe6b39-9feb-4c81-80af-608b33410e1a" />


### Consulta 1.3: Marcas distintas de productos con precio menor o igual a 250
1. **Pregunta del dominio:** ¿Cuáles son las marcas distintas de productos cuyo precio es menor o igual a 250?
2. **Expresión en álgebra relacional:**
   `π marca (σ precio ≤ 250 (productos))`
3. **Captura de RelaX (árbol y resultado):**
  <img width="652" height="540" alt="image" src="https://github.com/user-attachments/assets/b84a53b2-3f4c-4d65-8673-8f6e196fcf31" />
  <img width="645" height="539" alt="image" src="https://github.com/user-attachments/assets/02b6d850-a3ad-478b-a77e-0b1f6c4a519b" />

4. **SQL equivalente y comprobación:**
   ```sql
   SELECT DISTINCT marca
   FROM productos
   WHERE precio <= 250;

<img width="1081" height="728" alt="image" src="https://github.com/user-attachments/assets/8d7d62ff-a04d-48b2-830e-be0ef360fb5b" />

---

## Unión (∪), Diferencia (−) e Intersección (∩)

### Consulta 2.1: Códigos de barras en categoría o incluir (Unión)
1. **Pregunta del dominio:** ¿Cuáles son todos los códigos de barras (`cod_barra`) que aparecen ya sea en la tabla `categoria` o en la tabla `incluir`?
2. **Expresión en álgebra relacional:**
   ```text
   cods_categoria = π cod_barra (categoria)
   cods_incluir = π cod_barra (incluir)
   cods_categoria ∪ cods_incluir
   
<img width="654" height="536" alt="image" src="https://github.com/user-attachments/assets/486909b6-df5a-4a4e-8b90-3c7a8e4323b4" />
<img width="284" height="545" alt="image" src="https://github.com/user-attachments/assets/8f0d6995-09ea-4a9b-b816-533aba0fceaf" />
<img width="379" height="552" alt="image" src="https://github.com/user-attachments/assets/e3375d46-083b-4b50-af2d-4c7e10d35231" />
<img width="1085" height="725" alt="image" src="https://github.com/user-attachments/assets/eaf5c72e-f8b8-4f6a-bac1-44c55ce262aa" />


### Consulta 2.2: Códigos de barras en productos pero no en incluir (Diferencia)
1. **Pregunta del dominio:** ¿Qué códigos de barras (`cod_barra`) están registrados en `productos`, pero no aparecen en la tabla `incluir`?
2. **Expresión en álgebra relacional:**
   ```text
   cods_productos = π cod_barra (productos)
   cods_incluir = π cod_barra (incluir)
   cods_productos - cods_incluir

<img width="652" height="500" alt="image" src="https://github.com/user-attachments/assets/4453df90-c149-4d02-8617-eed128e591ee" />
<img width="655" height="552" alt="image" src="https://github.com/user-attachments/assets/3a048b8b-2b57-4558-b7c4-c103ab1e618e" />
<img width="1092" height="722" alt="image" src="https://github.com/user-attachments/assets/92e8354c-45d8-4adf-9401-a24789968533" />


### Consulta 2.3: Códigos de barras en categoría e incluir (Intersección)
1. **Pregunta del dominio:** ¿Qué códigos de barras (`cod_barra`) aparecen tanto en la tabla `categoria` como en la tabla `incluir`?
2. **Expresión en álgebra relacional:**
   ```text
   cods_categoria = π cod_barra (categoria)
   cods_incluir = π cod_barra (incluir)
   cods_categoria ∩ cods_incluir

<img width="662" height="551" alt="image" src="https://github.com/user-attachments/assets/0d5956d6-75af-4722-bf56-fedcab63d725" />
<img width="662" height="551" alt="image" src="https://github.com/user-attachments/assets/cff9561b-f1c0-40bc-b5e2-10809af56bb7" />
<img width="1096" height="726" alt="image" src="https://github.com/user-attachments/assets/040ff946-e1d1-40de-ae2d-c2b5ebb0e559" />

---

## Producto Cartesiano (×)

### Consulta 3.1: Combinaciones de categoría filtrada y ventas de diciembre de 2025
1. **Pregunta del dominio:** ¿Cuáles son todas las combinaciones posibles entre la categoría con `id_categoria = '1'` y las ventas de diciembre de 2025 (`mes = 12 ∧ anio = 2025`), mostrando el nombre de la categoría y el ticket de la venta?
2. **Expresión en álgebra relacional:**
   `π nombre, ticket ((σ id_categoria = '1' (categoria_catalogo)) x (σ mes = 12 ∧ anio = 2025 (venta)))`
3. **Captura de RelaX (árbol y resultado):**
   <img width="651" height="550" alt="image" src="https://github.com/user-attachments/assets/bc08e156-f001-4531-a752-37d729027981" />
   <img width="667" height="389" alt="image" src="https://github.com/user-attachments/assets/6beb1f50-66de-4f2e-8ab1-e54722cc595d" />

4. **SQL equivalente y comprobación:**
   ```sql
   SELECT c.nombre, v.ticket
   FROM (
       SELECT nombre
       FROM categoria_catalogo
       WHERE id_categoria = '1'
   ) AS c
   CROSS JOIN (
       SELECT ticket
       FROM venta
       WHERE mes = 12 AND anio = 2025
   ) AS v;

<img width="1098" height="729" alt="image" src="https://github.com/user-attachments/assets/75245a4d-9cf9-4874-aa90-e63b2efd2244" />


---

## Reunión / Join (⋈)

### Consulta 4.1: Detalle de productos incluidos en ventas (Reunión natural)
1. **Pregunta del dominio:** ¿Qué tickets, códigos de barras, nombres y precios de productos aparecen registrados en los renglones de venta (`incluir`)?
2. **Expresión en álgebra relacional:**
   `π ticket, cod_barra, nombre, precio (incluir natural join productos)`
3. **Captura de RelaX (árbol y resultado):**
   <img width="651" height="529" alt="image" src="https://github.com/user-attachments/assets/7bade2a4-9cdd-4827-959d-84afb230288c" />
   <img width="650" height="544" alt="image" src="https://github.com/user-attachments/assets/3f4c7fcc-8240-4b3f-9b64-f41fb7737c14" />
   <img width="660" height="356" alt="image" src="https://github.com/user-attachments/assets/5f2722e7-8050-4b41-bcb5-6849bf45e6aa" />

4. **SQL equivalente y comprobación:**
   ```sql
   SELECT i.ticket, i.cod_barra, p.nombre, p.precio
   FROM incluir AS i
   INNER JOIN productos AS p
       ON i.cod_barra = p.cod_barra;

<img width="1109" height="731" alt="image" src="https://github.com/user-attachments/assets/9629a9c0-57bc-4acb-bda3-229a70f5108c" />


### Consulta 4.2: Asociación de códigos de barras con su categoría del catálogo (Theta-Join)
1. **Pregunta del dominio:** ¿Qué códigos de barras (`cod_barra`) están asociados a cada categoría del catálogo y cuál es el nombre (`nombre`) de dicha categoría?
2. **Expresión en álgebra relacional:**
   `π cod_barra, nombre (categoria ⋈ identificador = id_categoria categoria_catalogo)`
3. **Captura de RelaX (árbol y resultado):**
  <img width="661" height="555" alt="image" src="https://github.com/user-attachments/assets/75858fd3-8f1b-4168-a5fc-fdba4ba8143f" />
  <img width="663" height="544" alt="image" src="https://github.com/user-attachments/assets/49242f67-2fec-410f-a683-6a2dce2136df" />

4. **SQL equivalente y comprobación:**
```sql
SELECT c.cod_barra, cc.nombre
FROM categoria AS c
INNER JOIN categoria_catalogo AS cc
    ON c.identificador = cc.id_categoria;
```

<img width="1071" height="735" alt="image" src="https://github.com/user-attachments/assets/7f340758-d29f-4583-9d2e-58bfd0673007" />


### Consulta 4.3: Ventas de 2025 y productos incluidos (Reunión natural con selección)
1. **Pregunta del dominio:** ¿Qué tickets de ventas del año `2025`, su total (`total`) y los códigos de barras de productos (`cod_barra`) incluidos aparecen registrados?
2. **Expresión en álgebra relacional:**
   `π ticket, total, cod_barra (σ anio = 2025 (venta natural join incluir))`
3. **Captura de RelaX (árbol y resultado):**
  <img width="657" height="559" alt="image" src="https://github.com/user-attachments/assets/1538d796-37cf-4a48-a12a-fed9746fc4e7" />
  <img width="652" height="555" alt="image" src="https://github.com/user-attachments/assets/85a71b01-95a1-4a36-9121-395225d59079" />

4. **SQL equivalente y comprobación:**
   ```sql
   SELECT v.ticket, v.total, i.cod_barra
   FROM venta AS v
   INNER JOIN incluir AS i
       ON v.ticket = i.ticket
   WHERE v.anio = 2025;
   ```

   <img width="1072" height="727" alt="image" src="https://github.com/user-attachments/assets/80688bba-562e-4f09-b1b7-2c85a00227d5" />

---

## Reunión Externa / Left Join (⟕)

### Consulta 5.1: Productos y su asociación con tickets de venta (Left Outer Join)
1. **Pregunta del dominio:** ¿Qué códigos de barras (`cod_barra`) y nombres (`nombre`) están registrados en `productos`, y en qué `ticket` de `incluir` aparecen (conservando todos los productos aunque no estén en `incluir`)?
2. **Expresión en álgebra relacional:**
   `π productos.cod_barra, productos.nombre, incluir.ticket (productos left join incluir)`
3. **Captura de RelaX (árbol y resultado):**
  <img width="651" height="540" alt="image" src="https://github.com/user-attachments/assets/89e66461-9d0f-4004-890f-f5446f398e61" />
  <img width="649" height="548" alt="image" src="https://github.com/user-attachments/assets/b897d2d9-1e31-4d0f-afff-80d77637b9a5" />
  <img width="649" height="558" alt="image" src="https://github.com/user-attachments/assets/08910597-99ee-4ea3-949e-ffd219ad353a" />

4. **SQL equivalente y comprobación:**
   ```sql
   SELECT p.cod_barra, p.nombre, i.ticket
   FROM productos AS p
   LEFT JOIN incluir AS i
       ON p.cod_barra = i.cod_barra;

<img width="1080" height="740" alt="image" src="https://github.com/user-attachments/assets/96800358-5e5e-4485-89ec-546d1207a9ec" />

### Consulta 5.2: Categorías del catálogo y códigos de barras asociados (Left Outer Join con condición)
1. **Pregunta del dominio:** ¿Qué categorías existen en `categoria_catalogo` (`id_categoria`, `nombre`) y qué códigos de barras (`cod_barra`) tienen asignados en `categoria`, conservando todas las categorías del catálogo aunque no tengan correspondencia?
2. **Expresión en álgebra relacional:**
   `π categoria_catalogo.id_categoria, categoria_catalogo.nombre, categoria.cod_barra (categoria_catalogo left join id_categoria = identificador categoria)`
3. **Captura de RelaX (árbol y resultado):**
   <img width="656" height="546" alt="image" src="https://github.com/user-attachments/assets/3baad014-38d0-4a3c-a40a-00c8bfc6bd73" />
   <img width="646" height="553" alt="image" src="https://github.com/user-attachments/assets/6e4454b5-605a-49e6-b3c2-0d57d478fbd2" />

4. **SQL equivalente y comprobación:**
   ```sql
   SELECT cc.id_categoria, cc.nombre, c.cod_barra
   FROM categoria_catalogo AS cc
   LEFT JOIN categoria AS c
       ON cc.id_categoria = c.identificador;

<img width="1077" height="737" alt="image" src="https://github.com/user-attachments/assets/ef4cc439-3771-4738-bfeb-7e08ea815a9d" />

---

## Renombramiento y Reunión (ρ, ⋈)

### Consulta 6: Reporte de renglones de venta con atributos renombrados de producto
1. **Pregunta del dominio:** ¿Cuáles son los tickets de venta (`ticket`), códigos de barras (`cod_barra`), nombres renombrados como `producto_nombre` y precios unitarios renombrados como `precio_unitario` de los productos incluidos en ventas?
2. **Expresión en álgebra relacional:**
   `π ticket, cod_barra, producto_nombre, precio_unitario (incluir ⋈ (ρ nombre -> producto_nombre, precio -> precio_unitario (productos)))`
3. **Captura de RelaX (árbol y resultado):**
   <img width="656" height="553" alt="image" src="https://github.com/user-attachments/assets/e7faca30-c43f-4180-b173-1e150a04f6f4" />
   <img width="650" height="548" alt="image" src="https://github.com/user-attachments/assets/943b0a95-86e4-47af-919e-4e9e5a6eabe5" />

4. **SQL equivalente y comprobación:**
   ```sql
   SELECT
       i.ticket,
       i.cod_barra,
       p.nombre AS producto_nombre,
       p.precio AS precio_unitario
   FROM incluir AS i
   INNER JOIN productos AS p
       ON i.cod_barra = p.cod_barra;

<img width="1081" height="733" alt="image" src="https://github.com/user-attachments/assets/1a479d6d-0d0e-4304-bddb-a0e34d4cd441" />





