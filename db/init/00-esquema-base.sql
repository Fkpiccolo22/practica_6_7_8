CREATE TABLE IF NOT EXISTS Categoria (
    cod_barra VARCHAR(50),
    identificador VARCHAR(50),
    nombre VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS productos (
    cod_barra VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100),
    marca VARCHAR(100),
    precio NUMERIC(12, 2)
);

CREATE TABLE IF NOT EXISTS venta (
    ticket VARCHAR(50) PRIMARY KEY,
    identificador_cliente VARCHAR(50),
    identificador_empleado VARCHAR(50),
    total NUMERIC(12, 2),
    dia INT,
    mes INT,
    anio INT
);

CREATE TABLE IF NOT EXISTS incluir (
    ticket VARCHAR(50),
    cod_barra VARCHAR(50)
);

INSERT INTO productos (cod_barra, nombre, marca, precio) VALUES
    ('750100000366', 'Articulo_366', 'Danone', 468.04),
    ('750100000005', 'Articulo_5', 'Danone', 412.77),
    ('750100000371', 'Articulo_371', 'Nestle', 693.97),
    ('750100000012', 'Articulo_12', 'Nestle', 307.56),
    ('750100000016', 'Articulo_16', 'Colgate', 480.08),
    ('750100000058', 'Articulo_58', 'Alpura', 417.87),
    ('750100000011', 'Articulo_11', 'Coca-Cola', 125.05),
    ('750100000007', 'Articulo_7', 'Colgate', 75.28),
    ('750100000003', 'Articulo_3', 'Danone', 470.97),
    ('750100000010', 'Articulo_10', 'Coca-Cola', 692.87),
    ('750100000456', 'Articulo_456', 'Coca-Cola', 817.67),
    ('750100000358', 'Articulo_358', 'Bimbo', 223.71),
    ('750100000120', 'Articulo_120', 'Bimbo', 230.22),
    ('750100000009', 'Articulo_9', 'Lala', 38.63),
    ('750100000320', 'Articulo_320', 'Unilever', 693.46),
    ('750100000138', 'Articulo_138', 'Alpura', 235.41),
    ('750100000019', 'Articulo_19', 'Danone', 123.54),
    ('750100000369', 'Articulo_369', 'Lala', 169.31),
    ('750100000104', 'Articulo_104', 'Alpura', 580.97),
    ('750100000001', 'Articulo_1', 'Unilever', 78.02)
ON CONFLICT (cod_barra) DO NOTHING;

INSERT INTO Categoria (cod_barra, identificador, nombre) VALUES
    ('750100000001', '5', 'Frutas y Verduras'),
    ('750100000003', '17', 'Cuidado Personal'),
    ('750100000005', '48', 'Lacteos'),
    ('750100000007', '10', 'Bebidas'),
    ('750100000009', '11', 'Bebidas'),
    ('750100000010', '4', 'Carnes'),
    ('750100000011', '50', 'Carnes'),
    ('750100000012', '1', 'Abarrotes'),
    ('750100000016', '48', 'Lacteos'),
    ('750100000019', '45', 'Lacteos'),
    ('750100000058', '48', 'Lacteos'),
    ('750100000104', '30', 'Bebidas'),
    ('750100000120', '2', 'Frutas y Verduras'),
    ('750100000138', '43', 'Lacteos'),
    ('750100000320', '49', 'Limpieza'),
    ('750100000358', '19', 'Abarrotes'),
    ('750100000366', '36', 'Lacteos'),
    ('750100000369', '12', 'Limpieza'),
    ('750100000371', '38', 'Limpieza'),
    ('750100000456', '31', 'Bebidas'),
    ('750100000001', 'CAT-01', 'Abarrotes');

INSERT INTO venta (ticket, identificador_cliente, identificador_empleado, total, dia, mes, anio) VALUES
    ('10015', '83', '239', 1737.75, 6, 7, 2025),
    ('10005', '151', '224', 1972.29, 25, 5, 2025),
    ('10014', '141', '234', 2023.04, 20, 1, 2025),
    ('10011', '154', '276', 787.92, 19, 7, 2025),
    ('10010', '41', '233', 593.91, 12, 12, 2025),
    ('10019', '8', '252', 3212.57, 14, 5, 2025),
    ('10017', '100', '203', 65.17, 11, 12, 2025),
    ('10007', '5', '235', 3297.36, 5, 3, 2025),
    ('10016', '176', '213', 538.28, 18, 5, 2025),
    ('10001', '42', '228', 242.73, 17, 12, 2025),
    ('10006', '19', '211', 1131.86, 3, 4, 2025),
    ('10013', '19', '278', 2171.37, 2, 8, 2025),
    ('10018', '156', '214', 620.40, 21, 8, 2025),
    ('10008', '8', '278', 1749.95, 16, 9, 2025),
    ('10009', '69', '255', 2094.37, 21, 11, 2025),
    ('10003', '83', '281', 848.53, 6, 8, 2025),
    ('10020', '174', '265', 3056.17, 20, 12, 2025),
    ('10004', '135', '290', 1635.33, 6, 8, 2025),
    ('10012', '27', '299', 2766.81, 26, 1, 2025),
    ('10002', '138', '235', 1293.91, 6, 1, 2025)
ON CONFLICT (ticket) DO NOTHING;

INSERT INTO incluir (ticket, cod_barra) VALUES
    ('10001', '750100000120'),
    ('10002', '750100000369'),
    ('10003', '750100000358'),
    ('10006', '750100000366'),
    ('10006', '750100000371'),
    ('10008', '750100000320'),
    ('10009', '750100000058'),
    ('10009', '750100000456'),
    ('10010', '750100000138'),
    ('10014', '750100000104'),
    ('10015', '750100000016');
