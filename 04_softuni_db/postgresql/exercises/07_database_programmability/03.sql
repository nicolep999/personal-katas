CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    set_of_letters VARCHAR(50),
    word VARCHAR(50)
)
    RETURNS BOOLEAN AS $$
DECLARE
    cleaned_word TEXT;
    char TEXT;
    letter_count INT;
    set_letter_count INT;
BEGIN
    cleaned_word := LOWER(regexp_replace(word, '[^a-z]', '', 'g'));
    set_of_letters := LOWER(set_of_letters);
    FOR char IN SELECT * FROM regexp_split_to_table(cleaned_word, '') LOOP
            SELECT COUNT(*) INTO letter_count FROM regexp_split_to_table(cleaned_word, '') AS c WHERE c = char;
            SELECT COUNT(*) INTO set_letter_count FROM regexp_split_to_table(set_of_letters, '') AS c WHERE c = char;
            IF letter_count > set_letter_count THEN
                RETURN FALSE;
            END IF;
        END LOOP;
    RETURN TRUE;
END;
$$ LANGUAGE plpgsql;