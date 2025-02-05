SELECT clients.full_name,
       COUNT(DISTINCT courses.car_id) AS count_of_cars,
       SUM(courses.bill)              AS total_sum
FROM clients
         JOIN courses ON clients.id = courses.client_id
WHERE clients.full_name LIKE '_a%'
GROUP BY clients.id, clients.full_name
HAVING COUNT(DISTINCT courses.car_id) > 1
ORDER BY clients.full_name;