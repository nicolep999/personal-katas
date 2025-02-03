SELECT first_name,
       last_name,
       make,
       model,
       mileage
from drivers
         JOIN cars_drivers ON drivers.id = cars_drivers.driver_id
         JOIN cars ON cars_drivers.car_id = cars.id
WHERE mileage IS NOT NULL
ORDER BY mileage DESC, first_name;