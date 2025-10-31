SELECT count(*)
FROM bookings
         JOIN customers ON bookings.customer_id = customers.customer_id
WHERE customers.last_name = 'Hahn';