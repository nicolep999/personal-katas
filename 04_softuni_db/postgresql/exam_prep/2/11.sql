CREATE TABLE search_results (
                                id SERIAL PRIMARY KEY,
                                address_name VARCHAR(50),
                                full_name VARCHAR(100),
                                level_of_bill VARCHAR(20),
                                make VARCHAR(30),
                                condition CHAR(1),
                                category_name VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE sp_courses_by_address(address_name VARCHAR(100))
    LANGUAGE plpgsql
AS
$$
BEGIN
    TRUNCATE TABLE search_results;
    INSERT INTO search_results (address_name, full_name, level_of_bill, make, condition, category_name)
    SELECT addresses.name,
           cl.full_name,
           CASE
               WHEN c.bill <= 20 THEN 'Low'
               WHEN c.bill <= 30 THEN 'Medium'
               ELSE 'High'
               END,
           car.make,
           car.condition,
           cat.name
    FROM courses c
             JOIN addresses on c.from_address_id = addresses.id
             JOIN clients cl ON c.client_id = cl.id
             JOIN cars car ON c.car_id = car.id
             JOIN categories cat ON car.category_id = cat.id
    WHERE addresses.name = address_name
    ORDER BY car.make, cl.full_name;
END;
$$;
