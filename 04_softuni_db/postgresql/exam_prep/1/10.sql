SELECT
    name as animal,
    TO_CHAR(birthdate, 'YYYY') AS birthdate,
    animal_type
FROM animals
JOIN animal_types ON animals.animal_type_id = animal_types.id
WHERE owner_id IS NULL
AND birthdate > '01/01/2017'
AND animal_type_id != 3
ORDER BY name