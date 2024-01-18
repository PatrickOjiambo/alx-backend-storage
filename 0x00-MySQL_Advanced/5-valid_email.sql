--SQL script that creates a trigger that resets the
-- attribute valid_email only when the email has been changed.
CREATE TRIGGER validate_email AFTER
UPDATE ON users FOR EACH ROW
BEGIN IF NEW.email != OLD.valid_email THEN NEW.valid_email = 0 END IF;

END