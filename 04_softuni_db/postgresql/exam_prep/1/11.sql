CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(
    searched_volunteers_department VARCHAR(30)
)
    RETURNS INT AS $$
DECLARE
    volunteer_count INT;
BEGIN
    SELECT COUNT(*) INTO volunteer_count
    FROM volunteers v
             JOIN volunteers_departments d ON v.department_id = d.id
    WHERE d.department_name = searched_volunteers_department;

    RETURN volunteer_count;
END;
$$ LANGUAGE plpgsql;

SELECT fn_get_volunteers_count_from_department('Zoo events')