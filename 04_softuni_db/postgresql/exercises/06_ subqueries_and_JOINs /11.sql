SELECT country_code,
       mountain_range,
       peak_name,
       elevation
FROM mountains
         FULL JOIN peaks
                   ON mountains.id = peaks.mountain_id
         FULL JOIN mountains_countries
                   ON mountains.id = mountains_countries.mountain_id
WHERE peaks.elevation > 2835
  AND country_code = 'BG'
ORDER BY elevation DESC
