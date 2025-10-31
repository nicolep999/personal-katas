SELECT country_code,
       count(*) as mountain_range_count
FROM mountains_countries
         JOIN mountains ON mountains_countries.mountain_id = mountains.id
WHERE country_code IN ('BG', 'RU', 'US')
GROUP BY country_code
ORDER BY mountain_range_count DESC
