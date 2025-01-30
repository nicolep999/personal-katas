CREATE TABLE notification_emails
(
    id           SERIAL PRIMARY KEY,
    recipient_id INT          NOT NULL,
    subject      VARCHAR(255) NOT NULL,
    body         TEXT         NOT NULL
);


CREATE OR REPLACE FUNCTION trigger_fn_send_email_on_balance_change()
    RETURNS TRIGGER AS
$$
BEGIN
    INSERT INTO notification_emails (recipient_id, subject, body)
    VALUES (NEW.account_id,
            'Balance change for account: ' || NEW.account_id,
            'On ' || NOW()::DATE || ' your balance was changed from ' || OLD.new_sum || ' to ' || NEW.new_sum);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_send_email_on_balance_change
    AFTER UPDATE
    ON logs
    FOR EACH ROW
    WHEN (OLD.new_sum IS DISTINCT FROM NEW.new_sum)
EXECUTE FUNCTION trigger_fn_send_email_on_balance_change();
