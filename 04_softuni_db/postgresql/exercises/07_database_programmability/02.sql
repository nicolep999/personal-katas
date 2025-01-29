CREATE OR REPLACE FUNCTION fn_calculate_future_value(
    initial_sum DECIMAL(18,6),
    yearly_interest_rate DECIMAL(18,6),
    number_of_years INTEGER
)
    RETURNS DECIMAL AS $$
BEGIN
    RETURN TRUNC(initial_sum * ((1 + yearly_interest_rate) ^ number_of_years), 4);
END;
$$ LANGUAGE plpgsql;