SELECT b.booking_id,
       a.name                                    AS apartment_owner,
       a.apartment_id,
       concat_ws(' ', c.first_name, c.last_name) AS customer_name
FROM bookings as b
         FULL JOIN customers as c ON b.customer_id = c.customer_id
         FULL JOIN apartments as a ON b.booking_id = a.booking_id
ORDER BY b.booking_id, apartment_owner, customer_name
