UPDATE cars
SET condition = 'C'
WHERE make != 'Mercedes-Benz'
    AND (mileage >= 800000
   OR mileage is null)
    AND year <= 2010;