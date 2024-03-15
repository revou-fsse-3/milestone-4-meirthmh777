CREATE DATABASE mbanking_app;
USE mbanking_app;

CREATE TABLE users(
	id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
ALTER TABLE users
MODIFY created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
MODIFY updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
ALTER TABLE users
MODIFY username VARCHAR(255) NOT NULL UNIQUE,
MODIFY email VARCHAR(255) NOT NULL UNIQUE;
ALTER TABLE users
RENAME COLUMN password_hash to password;

INSERT INTO users (username, email, password)
VALUES ('mei', 'mei@gmail.com', 'halo12345');
SELECT * FROM users;

CREATE TABLE accounts (
	id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    account_type VARCHAR(255),
    account_number VARCHAR(255),
    balance DECIMAL(10,2),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE transactions (
	id INT PRIMARY KEY AUTO_INCREMENT,
	from_account_id INT,
    to_account_id INT,
    amount DECIMAL(10,2),
    type_transaction VARCHAR(255),
    description_transaction VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (from_account_id) REFERENCES accounts(id),
    FOREIGN KEY (to_account_id) REFERENCES accounts(id)
);


