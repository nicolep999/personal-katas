SELECT country_name,
       river_name
FROM countries
         FULL JOIN countries_rivers
                   ON countries.country_code = countries_rivers.country_code
         FULL JOIN rivers
                   ON countries_rivers.river_id = rivers.id
WHERE continent_code = 'AF'
ORDER BY country_name
LIMIT 5;