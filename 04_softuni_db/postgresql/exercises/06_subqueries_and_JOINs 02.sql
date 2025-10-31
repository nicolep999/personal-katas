SELECT
    a.name,
    a.country,
    cast(b.booked_at AS date)
FROM apartments as a
    LEFT JOIN bookings as b ON a.booking_id = b.booking_id
    LIMIT 10
