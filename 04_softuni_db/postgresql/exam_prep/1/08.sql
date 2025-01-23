SELECT
    concat_ws(' - ', o.name, a.name) AS "owner - animal",
    o.phone_number,
    c.cage_id AS cage_id
FROM owners o
         JOIN animals a ON o.id = a.owner_id
         JOIN animals_cages c ON a.id = c.animal_id
         JOIN animal_types at ON a.animal_type_id = at.id
WHERE at.animal_type = 'Mammals'
ORDER BY o.name , a.name DESC;