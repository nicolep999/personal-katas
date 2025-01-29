CREATE FUNCTION fn_full_name(first_name VARCHAR(50), last_name VARCHAR(50))
RETURNS VARCHAR(100)
AS $$
BEGIN
    RETURN COALESCE(
        CASE WHEN first_name IS NULL THEN NULL END,
        CASE WHEN last_name IS NULL THEN initcap(first_name) ELSE initcap(first_name) || ' ' || initcap(last_name) END
    );
END;
$$ LANGUAGE plpgsql;


/*

CREATE FUNCTION fn_full_name(first_name VARCHAR(50), last_name VARCHAR(50))
RETURNS VARCHAR(100)
AS $$
DECLARE my_string VARCHAR(100);
BEGIN
    IF first_name IS NULL THEN
        my_string := initcap(last_name);
    END IF;
    IF last_name IS NULL THEN
        my_string := initcap(first_name);
    ELSE
        my_string := initcap(first_name) || ' ' || initcap(last_name);
    END IF;
    RETURN my_string;
END;
$$ LANGUAGE plpgsql;

*/