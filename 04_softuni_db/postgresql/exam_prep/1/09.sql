SELECT
    volunteers.name as volunteers,
    phone_number,
    (SUBSTRING(TRIM(address) FROM LENGTH('Sofia, ') + 1)) AS address_in_sofia
FROM volunteers WHERE department_id = 2 AND address LIKE '%Sofia%'
ORDER BY name