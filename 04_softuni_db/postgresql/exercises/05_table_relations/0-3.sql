-- 01

CREATE TABLE products (
    product_name VARCHAR(100)
);

INSERT INTO products (product_name)
VALUES ('Broccoli'),
       ('Shampoo'),
       ('Toothpaste'),
       ('Candy');

ALTER TABLE products
    ADD COLUMN id SERIAL PRIMARY KEY;

-- 02

ALTER TABLE products
    DROP COLUMN id;

-- 03

CREATE DATABASE customs_db;

CREATE TABLE passports (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY (START WITH 100 INCREMENT by 1),
    nationality VARCHAR(50)
);

INSERT INTO passports (nationality)
    VALUES
        ('N34FG21B'),
        ('K65LO4R7'),
        ('ZE657QP2' );

CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    salary DECIMAL(10, 2),
    passport_id INTEGER,
    CONSTRAINT fk_passport_id FOREIGN KEY (passport_id) REFERENCES passports (id)
);

INSERT INTO people (first_name, salary, passport_id)
    VALUES
	('Roberto', 43300.0000, 101),
    ('Tom', 56100.0000, 102),
    ('Yana', 60200.0000, 100);
