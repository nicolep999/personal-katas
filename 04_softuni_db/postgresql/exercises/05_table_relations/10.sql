CREATE TABLE item_types
(
    id             SERIAL PRIMARY KEY,
    item_type_name VARCHAR(255)
);

CREATE TABLE items
(
    id           serial PRIMARY KEY,
    item_name    VARCHAR(255),
    item_type_id INTEGER REFERENCES item_types (id)
);

CREATE TABLE cities
(
    id        SERIAL PRIMARY KEY,
    city_name VARCHAR(255)
);

CREATE TABLE customers
(
    id            SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    birthday      DATE,
    city_id       INTEGER REFERENCES cities (id)
);

CREATE TABLE orders
(
    id          SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers (id)
);

CREATE TABLE order_items
(
    order_id INTEGER REFERENCES orders (id),
    item_id  INTEGER REFERENCES items (id)
);



