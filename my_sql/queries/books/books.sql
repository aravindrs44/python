INSERT INTO authors(name, created_at, updated_at)
VALUES("Jane Austen", NOW(), NOW());

INSERT INTO authors(name, created_at, updated_at)
VALUES("Fyodor Dostoevsky", NOW(), NOW());

INSERT INTO authors(name, created_at, updated_at)
VALUES("Emily Dickinson", NOW(), NOW());

INSERT INTO authors(name, created_at, updated_at)
VALUES("William Shakespeare", NOW(), NOW());

INSERT INTO authors(name, created_at, updated_at)
VALUES("Lau Tzu", NOW(), NOW());

INSERT INTO books(title, num_of_pages, created_at, updated_at)
VALUES("C Sharp", 1057, NOW(), NOW());

INSERT INTO books(title, num_of_pages, created_at, updated_at)
VALUES("Java", 894, NOW(), NOW());

INSERT INTO books(title, num_of_pages, created_at, updated_at)
VALUES("Python", 1, NOW(), NOW());

INSERT INTO books(title, num_of_pages, created_at, updated_at)
VALUES("PHP", 5, NOW(), NOW());

INSERT INTO books(title, num_of_pages, created_at, updated_at)
VALUES("Ruby", 543, NOW(), NOW());

UPDATE books SET title = "C#"
WHERE id = 1;

UPDATE authors SET name = "Bill Shakespeare"
WHERE id = 4;

INSERT INTO favorites(authors_id, books_id)
VALUES
(1, 1), (1, 2),
(2, 1), (2, 2), (2, 3),
(3, 1), (3, 2), (3, 3), (3, 4),
(4, 1), (4, 2), (4, 3), (4, 4), (4, 5);

SELECT * FROM authors
JOIN favorites ON authors.id =  favorites.authors_id
JOIN books ON books.id = favorites.books_id
WHERE books.id = 3;

DELETE FROM favorites
WHERE books_id = 3 
LIMIT 1;

INSERT INTO favorites(authors_id, books_id)
VALUES(5, 2);

SELECT * FROM favorites
WHERE authors_id = 3;

SELECT * FROM favorites
WHERE books_id = 5;







