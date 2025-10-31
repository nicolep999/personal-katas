SELECT b.booking_id,
       DATE(b.starts_at)                      AS starts_at,
       b.apartment_id,
       CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM customers c
         LEFT JOIN bookings b ON c.customer_id = b.customer_id
ORDER BY customer_name
LIMIT 10;
