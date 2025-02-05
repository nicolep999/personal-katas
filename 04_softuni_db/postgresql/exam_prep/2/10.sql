CREATE OR REPLACE FUNCTION fn_courses_by_client(
    IN phone_num VARCHAR(20)
)
    RETURNS INT
    LANGUAGE plpgsql
AS
$$
DECLARE
    course_count INT;
BEGIN
    SELECT COUNT(*)
    INTO course_count
    FROM clients
             JOIN courses ON clients.id = courses.client_id
    WHERE phone_number = phone_num;
    RETURN course_count;
END;
$$;