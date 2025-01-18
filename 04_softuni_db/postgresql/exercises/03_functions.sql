-- 00
CREATE DATABASE geography_db;

-- 01

CREATE VIEW view_river_info AS
    SELECT
        concat_ws(' ', 'The river', river_name, 'flows into the',  outflow, 'and is', length, 'kilometers long.') AS "River Information"
    FROM rivers ORDER BY river_name;

-- 02

CREATE VIEW view_continents_countries_currencies_details AS
    SELECT
        concat_ws(': ', continent_name, continents.continent_code) AS continent_details,
        concat_ws(' - ', country_name, capital, area_in_sq_km, 'km2') AS country_information,
        concat(description,' (', currencies.currency_code,')') AS currencies
    FROM continents, countries, currencies
    WHERE continents.continent_code = countries.continent_code AND countries.currency_code = currencies.currency_code
    ORDER BY country_information, currencies;

-- 03

ALTER TABLE  countries
ADD COLUMN capital_code CHAR(2);
UPDATE countries
SET capital_code = SUBSTRING(capital, 1, 2);

-- 04

SELECT
    substring(description, 5)
FROM currencies;

-- 05

SELECT
    substring("River Information", '([0-9]{1,4})') AS river_length
FROM
    view_river_info;

-- 06

SELECT
    REPLACE(mountain_range, 'a', '@') AS replace_a,
    REPLACE(mountain_range, 'A', '$') AS replace_A
FROM
    mountains;

-- 07

SELECT
    capital,
    TRANSLATE(capital, 'áãåçéíñóú', 'aaaceinou') AS translated_name
FROM countries

-- 08

SELECT
    continent_name,
    TRIM(continent_name) as trim
FROM continents;

-- 09

SELECT
    continent_name,
    TRIM(trailing from continent_name) as trim
FROM continents

-- 10

SELECT
    LTRIM(peak_name, 'M') AS left_trim,
    RTRIM(peak_name, 'm') AS right_trim
FROM
    peaks;

-- 11

SELECT
    CONCAT(mountain_range, ' ', peak_name) AS mountain_information,
    CHAR_LENGTH(CONCAT(mountain_range, ' ', peak_name)) AS characters_length,
    BIT_LENGTH(CONCAT(mountain_range, ' ', peak_name)) AS bits_of_a_tring
FROM mountains ,peaks  WHERE mountains.id = peaks.mountain_id;

-- 12

SELECT
    population,
    LENGTH(CAST(population AS VARCHAR)) AS "length"
FROM countries;

-- 13

SELECT
    peak_name,
    LEFT(peak_name, 4) AS positive_left,
    LEFT(peak_name, -4) AS negative_left
FROM peaks

-- 14

SELECT
    peak_name,
    RIGHT(peak_name, 4) AS positive_right,
    RIGHT(peak_name, -4) AS negative_right
FROM peaks;

--15

UPDATE countries
SET iso_code = upper(left(country_name, 3))
WHERE iso_code IS NULL;

-- 16

UPDATE countries
SET country_code = lower((reverse(country_code)));

-- 17

SELECT
    concat_ws(' ', elevation, repeat('-',  3 )|| repeat('>', 2), peak_name) AS "Elevation -->> Peak Name"
FROM peaks WHERE elevation >= 4884
;

-- 18.01

CREATE DATABASE bookings_db;

-- 18.02

CREATE TABLE bookings_calculation AS
    SELECT
        booked_for,
        CAST(booked_for * 50 AS NUMERIC) AS multiplication,
        CAST(booked_for % 50 AS NUMERIC) AS modulo
FROM bookings WHERE  apartment_id = 93;

-- 19

SELECT
    latitude,
    ROUND(latitude, 2) AS round,
    TRUNC(latitude, 2) AS trunc
FROM apartments;

-- 20

SELECT
    longitude,
    ABS(longitude) AS abs
FROM apartments;

-- 21

ALTER TABLE bookings
ADD COLUMN
	billing_day TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP;

SELECT
    TO_CHAR(billing_day, 'DD "Day" MM "Month" YYYY "Year" HH24:MI:SS')
FROM
    bookings;

-- 22

SELECT
    extract(YEAR FROM booked_at) AS YEAR,
    extract(MONTH FROM booked_at) AS MONTH,
    extract(DAY FROM booked_at) AS DAY,
    extract(HOUR FROM booked_at) AS HOUR,
    extract(MINUTE FROM booked_at) AS MINUTE,
    ceil(extract(SECOND FROM booked_at)) AS SECOND
FROM
    bookings;

-- 23

SELECT
    user_id,
    age(starts_at, booked_at) AS "Early Birds"
FROM
    bookings
WHERE
    starts_at - booked_at >= '10 MONTHS';

-- 24

SELECT
    companion_full_name,
    email
FROM
    users WHERE companion_full_name ILIKE '%and%'
  AND
    email NOT LIKE '%@gmail';

-- 25

SELECT
    LEFT(first_name, 2) AS initials,
    COUNT('initials') AS user_count
FROM
    users GROUP BY initials
ORDER BY
    user_count DESC,
    initials;

-- 26

SELECT
    SUM(booked_for) AS total_value
FROM
    bookings
WHERE
    apartment_id = 90;

-- 27

SELECT
    AVG(multiplication) AS avarage_value
FROM
    bookings_calculation;