SELECT
    mountain_range,
    peak_name,
    elevation
FROM mountains JOIN peaks
    ON mountains.id = peaks.mountain_id
    WHERE mountain_range LIKE 'Rila'
    ORDER BY elevation DESC