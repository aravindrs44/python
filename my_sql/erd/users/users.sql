USE users_schema;

INSERT INTO	users (created_at, updated_at, first_name, last_name, email)
VALUES (NOW(), NOW(), "Aravind", "Sripada", "aravindrs@hotmail.com");

INSERT INTO	users (created_at, updated_at, first_name, last_name, email)
VALUES (NOW(), NOW(), "Bob", "The Builder", "bob@thebuilder.com");

INSERT INTO	users (created_at, updated_at, first_name, last_name, email)
VALUES (NOW(), NOW(), "Mewtwo", "Strikes Back", "ash@stone.com");

SELECT * FROM users;

SELECT * FROM users
WHERE email = "aravindrs@hotmail.com";

SELECT * FROM users
WHERE id = 3;

UPDATE users SET last_name = "Pancakes"
WHERE id = 3;

DELETE FROM users WHERE id = 2;

SELECT * FROM users
ORDER BY first_name;

SELECT * FROM users
ORDER BY first_name DESC;