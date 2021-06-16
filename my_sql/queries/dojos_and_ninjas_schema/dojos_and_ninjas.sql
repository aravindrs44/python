USE dojos_and_ninjas_schema;

INSERT INTO dojos(name, created_at, updated_at)
VALUES("Dojo at Bellevue", NOW(), NOW());

INSERT INTO dojos(name, created_at, updated_at)
VALUES("Dojo at Chicago", NOW(), NOW());

INSERT INTO dojos(name, created_at, updated_at)
VALUES("Dojo at Las Vegas", NOW(), NOW());

DELETE FROM dojos 
WHERE id > 0;

INSERT INTO dojos(name, created_at, updated_at)
VALUES("Dojo at Bellevue", NOW(), NOW());

INSERT INTO dojos(name, created_at, updated_at)
VALUES("Dojo at Chicago", NOW(), NOW());

INSERT INTO dojos(name, created_at, updated_at)
VALUES("Dojo at Boise", NOW(), NOW());

INSERT INTO ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES("Aravind", "Sripada", 23, NOW(), NOW(), 4);

INSERT INTO ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES("Brayan", "Navarro", 27, NOW(), NOW(), 4);

INSERT INTO ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES("Anthony", "Park", 23, NOW(), NOW(), 4);

INSERT INTO ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES("Pokemon", "Diamond", 15, NOW(), NOW(), 5);

INSERT INTO ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES("Pokemon", "Sword", 2, NOW(), NOW(), 5);

INSERT INTO ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES("Pokemon", "Emerald", 16, NOW(), NOW(), 5);

INSERT INTO ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES("Pokemon", "Colosseum", 17, NOW(), NOW(), 6);

INSERT INTO ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES("Pokemon", "Battle Revolution", 15, NOW(), NOW(), 6);

INSERT INTO ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES("Pokemon", "Go", 4, NOW(), NOW(), 6);

SELECT * FROM ninjas
WHERE dojo_id = 4;

SELECT * FROM ninjas
WHERE dojo_id = 6;

SELECT dojos.name FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
ORDER BY ninjas.id DESC
LIMIT 1;





