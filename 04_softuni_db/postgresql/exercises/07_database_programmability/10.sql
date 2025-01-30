CREATE OR REPLACE PROCEDURE sp_transfer_money(
    IN sender_id INT,
    IN receiver_id INT,
    IN amount NUMERIC(10, 4)
) AS
$$
BEGIN
    BEGIN
        CALL sp_withdraw_money(sender_id, amount);
        CALL sp_deposit_money(receiver_id, amount);
    EXCEPTION
        WHEN OTHERS THEN
            ROLLBACK;
            RETURN;
    END;
END;
$$ LANGUAGE plpgsql;