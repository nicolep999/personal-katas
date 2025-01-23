SELECT
    a.name AS animal_name,
    t.animal_type,
    TO_CHAR(a.birthdate, 'DD.MM.YYYY') AS birthdate
FROM
    animals a
        JOIN
    animal_types t ON a.animal_type_id = t.id
ORDER BY
    a.name;
