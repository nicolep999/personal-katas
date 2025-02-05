SELECT addresses.name       as address,
       CASE
           WHEN EXTRACT(hour FROM courses.start) BETWEEN 6 and 20 THEN 'Day'
           ELSE 'Night' END AS day_time,
       bill,
       full_name,
       make,
       model,
       categories.name      as category
FROM addresses
         JOIN courses ON addresses.id = courses.from_address_id
         JOIN clients ON courses.client_id = clients.id
         JOIN cars ON courses.car_id = cars.id
         JOIN categories ON cars.category_id = categories.id
ORDER BY courses.id;