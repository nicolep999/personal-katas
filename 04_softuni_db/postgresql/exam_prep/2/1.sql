CREATE TABLE addresses
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE categories
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR(10) NOT NULL
);

CREATE TABLE clients
(
    id           SERIAL PRIMARY KEY,
    full_name    VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE drivers
(
    id         SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name  VARCHAR(30) NOT NULL,
    age        INT         NOT NULL CHECK (age > 0),
    rating     NUMERIC(3, 2) DEFAULT 5.5
);

CREATE TABLE cars
(
    id          SERIAL PRIMARY KEY,
    make        VARCHAR(20) NOT NULL,
    model       VARCHAR(20),
    year        INT         NOT NULL CHECK (year > 0) DEFAULT 1,
    mileage     INT CHECK (mileage > 0)               DEFAULT 1,
    condition   CHAR(1)     NOT NULL,
    category_id INT         NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE courses
(
    id              SERIAL PRIMARY KEY,
    from_address_id INT       NOT NULL,
    FOREIGN KEY (from_address_id) REFERENCES addresses (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    start           TIMESTAMP NOT NULL,
    bill            NUMERIC(10, 2) DEFAULT 10 CHECK (bill > 0),
    car_id          INT       NOT NULL,
    FOREIGN KEY (car_id) REFERENCES cars (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    client_id       INT       NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE cars_drivers
(
    car_id    INT NOT NULL,
    driver_id INT NOT NULL,
    FOREIGN KEY (car_id) REFERENCES cars (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (driver_id) REFERENCES drivers (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);