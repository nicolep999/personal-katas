SELECT cars.id                     AS car_id,
       cars.make,
       cars.mileage,
       COUNT(courses.id)           AS count_of_courses,
       ROUND(AVG(courses.bill), 2) AS average_bill
FROM cars
         LEFT JOIN courses ON cars.id = courses.car_id
GROUP BY cars.id, cars.make, cars.model
HAVING COUNT(courses.id) != 2
ORDER BY count_of_courses DESC, cars.id;