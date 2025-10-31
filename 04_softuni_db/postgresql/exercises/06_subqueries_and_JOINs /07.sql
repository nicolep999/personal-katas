SELECT apartment_id,
       booked_for,
       first_name,
       country
FROM bookings
         INNER JOIN customers
                    ON bookings.customer_id = customers.customer_id
WHERE job_type LIKE '%Lead%'