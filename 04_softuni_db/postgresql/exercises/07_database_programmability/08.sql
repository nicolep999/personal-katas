CREATE PROCEDURE sp_deposit_money(
    IN account_id INT,
    IN money_amount NUMERIC(10, 4))
AS
$$
BEGIN
    UPDATE accounts
    SET balance = balance + money_amount
    WHERE id = account_id;
    COMMIT;
END;
$$
    LANGUAGE plpgsql
