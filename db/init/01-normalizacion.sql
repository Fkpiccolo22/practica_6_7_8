BEGIN;

ALTER TABLE Venta
    DROP COLUMN IF EXISTS Empleadoventas;

CREATE TABLE IF NOT EXISTS Categoria_Catalogo (
    Id_Categoria VARCHAR(50) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL
);

INSERT INTO Categoria_Catalogo (Id_Categoria, Nombre)
SELECT DISTINCT Identificador, Nombre
FROM Categoria
ON CONFLICT (Id_Categoria) DO NOTHING;

ALTER TABLE Categoria
    ADD CONSTRAINT fk_categoria_catalogo
        FOREIGN KEY (Identificador) REFERENCES Categoria_Catalogo (Id_Categoria)
        ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE Categoria
    DROP COLUMN IF EXISTS Nombre;

COMMIT;
