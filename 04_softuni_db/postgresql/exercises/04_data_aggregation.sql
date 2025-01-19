-- 01

SELECT count(*) FROM wizard_deposits;

-- 02

SELECT sum(deposit_amount) FROM wizard_deposits;

-- 03

SELECT round(avg(magic_wand_size), 3) FROM wizard_deposits;

-- 04

SELECT min(deposit_charge) FROM wizard_deposits;

-- 05

SELECT max(age) FROM wizard_deposits;

-- 06

SELECT
    deposit_group,
    sum(deposit_interest) FROM wizard_deposits
GROUP BY deposit_group
ORDER BY sum(deposit_interest) DESC;

-- 07

SELECT
    magic_wand_creator,
    min(magic_wand_size) AS minimum_wand_size
FROM wizard_deposits
GROUP BY magic_wand_creator
ORDER BY minimum_wand_size
LIMIT 5;

-- 08

SELECT
    deposit_group,
    is_deposit_expired,
    floor(avg(deposit_interest))
FROM wizard_deposits
WHERE deposit_start_date > '1985-01-01'
GROUP BY deposit_group, is_deposit_expired
ORDER BY deposit_group DESC;

-- 09

SELECT last_name,
       COUNT(*) AS notes_with_dumbledore
FROM wizard_deposits
WHERE notes LIKE '%Dumbledore%'
GROUP BY last_name;

-- 10

CREATE VIEW view_wizard_deposits_with_expiration_date_before_1983_08_17 AS
    SELECT
        concat_ws(' ', first_name, last_name) AS wizard_name,
        deposit_start_date AS start_date,
        deposit_expiration_date AS expiration_date,
        deposit_amount AS amount
FROM wizard_deposits
WHERE deposit_expiration_date <= '1983-08-17'
GROUP BY wizard_name, start_date, expiration_date, amount
ORDER BY expiration_date;

-- 11

SELECT
    magic_wand_creator,
    MAX(deposit_amount) AS max_deposit_amount
FROM wizard_deposits
GROUP BY magic_wand_creator
HAVING MAX(deposit_amount) < 20000 OR MAX(deposit_amount) > 40000
ORDER BY max_deposit_amount DESC
LIMIT 3;

-- 12

SELECT
    CASE
        WHEN age BETWEEN 0 AND 10 THEN '[0-10]'
        WHEN age BETWEEN 11 AND 20 THEN '[11-20]'
        WHEN age BETWEEN 21 AND 30 THEN '[21-30]'
        WHEN age BETWEEN 31 AND 40 THEN '[31-40]'
        WHEN age BETWEEN 41 AND 50 THEN '[41-50]'
        WHEN age BETWEEN 51 AND 60 THEN '[51-60]'
        ELSE '[61+]'
        END AS age_group,
    COUNT(*) AS count
FROM wizard_deposits
GROUP BY age_group
ORDER BY age_group;

-- 13

SELECT
    SUM(CASE WHEN department_id = 1 THEN 1 ELSE 0 END) AS Engineering,
    SUM(CASE WHEN department_id = 2 THEN 1 ELSE 0 END) AS "Tool Design",
    SUM(CASE WHEN department_id = 3 THEN 1 ELSE 0 END) AS Sales,
    SUM(CASE WHEN department_id = 4 THEN 1 ELSE 0 END) AS Marketing,
    SUM(CASE WHEN department_id = 5 THEN 1 ELSE 0 END) AS Purchasing,
    SUM(CASE WHEN department_id = 6 THEN 1 ELSE 0 END) AS "Research and Development",
    SUM(CASE WHEN department_id = 7 THEN 1 ELSE 0 END) AS Production
FROM employees;

-- 14

UPDATE employees
SET
    salary = CASE
                 WHEN hire_date < '2015-01-16' THEN salary + 2500
                 WHEN hire_date < '2020-03-04' THEN salary + 1500
                 ELSE salary
        END,
    job_title = CASE
                    WHEN hire_date < '2015-01-16' THEN CONCAT('Senior ', job_title)
                    WHEN hire_date < '2020-03-04' THEN CONCAT('Mid-', job_title)
                    ELSE job_title
        END;

-- 15

SELECT job_title,
       CASE
           WHEN AVG(salary) > 45800 THEN 'Good'
           WHEN AVG(salary) BETWEEN 27500 AND 45800 THEN 'Medium'
           WHEN AVG(salary) < 27500 THEN 'Need Improvement'
           END AS category
FROM employees
GROUP BY job_title
ORDER BY category, job_title;

-- 16

SELECT project_name,
       CASE
           WHEN start_date IS NULL AND end_date IS NULL THEN 'Ready for development'
           WHEN start_date IS NOT NULL AND end_date IS NULL THEN 'In Progress'
           ELSE 'Done'
           END AS project_status
FROM projects
WHERE project_name LIKE '%Mountain%';

-- 17

SELECT department_id,
       COUNT(*) AS num_employees,
       CASE
           WHEN AVG(salary) > 50000 THEN 'Above average'
           WHEN AVG(salary) <= 50000 THEN 'Below average'
           END AS salary_level
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 30000
ORDER BY department_id;