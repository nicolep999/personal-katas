SELECT
    owners.name,
    count('*') as count_of_animals
FROM owners JOIN public.animals a on owners.id = a.owner_id
group by owners.name
ORDER BY count_of_animals DESC , owners.name
LIMIT 5