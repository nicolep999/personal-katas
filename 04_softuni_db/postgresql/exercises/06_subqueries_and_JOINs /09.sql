SELECT name,
       sum(booked_for)
FROM apartments
         JOIN bookings
              ON apartments.apartment_id = bookings.apartment_id
GROUP BY name
ORDER BY name