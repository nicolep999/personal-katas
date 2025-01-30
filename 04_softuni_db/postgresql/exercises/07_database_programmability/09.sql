CREATE OR REPLACE PROCEDURE sp_withdraw_money(
    IN account_id INT,
    IN money_amount NUMERIC(10, 4)
)
AS
$$
DECLARE
    account_balance NUMERIC;
BEGIN
    SELECT balance FROM accounts WHERE id = account_id INTO account_balance;
    IF account_balance < money_amount THEN
        RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
        RETURN;
    END IF;
    UPDATE accounts SET balance = balance - money_amount WHERE id = account_id;
    COMMIT;
END;
$$
    LANGUAGE plpgsql;