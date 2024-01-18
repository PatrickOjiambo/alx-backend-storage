-- SQL script that creates a trigger that
-- decreases the quantity of an item after adding a new order.
CREATE TRIGGER decrease_item AFTER
INSERT
    ON orders FOR EACH ROW
UPDATE items
SET
    quantity = NEW.number - 1
WHERE
    name = NEW.item_name;