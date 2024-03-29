--creates a table users following these requirements:
--check holberton for the requirements
CREATE TABLE
    IF NOT EXISTS users (
        id INT NOT NULL AUTO_INCREMENT,
        email VARCHAR(255) NOT NULL,
        name VARCHAR(255),
        country ENUM ('US', 'CO', 'TN') DEFAULT 'US' NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (email)
    );