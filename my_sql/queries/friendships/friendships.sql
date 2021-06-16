INSERT INTO users(created_at, updated_at, first_name, last_name)
VALUES
(NOW(), NOW(), "Mario", "Mario"),
(NOW(), NOW(), "Kakashi", "Hatake"),
(NOW(), NOW(), "Monkey", "D. Luffy"),
(NOW(), NOW(), "Obi-Wan", "Kenobi"),
(NOW(), NOW(), "Renee", "Blasey"),
(NOW(), NOW(), "Natalie", "Paquette");

INSERT INTO friendships(created_at, updated_at, user_id, friend_id)
VALUES
(NOW(), NOW(), 1, 2),
(NOW(), NOW(), 1, 4),
(NOW(), NOW(), 1, 6),
(NOW(), NOW(), 2, 1),
(NOW(), NOW(), 2, 3),
(NOW(), NOW(), 2, 5),
(NOW(), NOW(), 3, 2),
(NOW(), NOW(), 3, 5),
(NOW(), NOW(), 4, 3),
(NOW(), NOW(), 5, 1),
(NOW(), NOW(), 5, 6),
(NOW(), NOW(), 6, 2),
(NOW(), NOW(), 6, 3);

SELECT users.first_name, users.last_name, user2.first_name, user2.last_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id;

SELECT users.first_name, users.last_name FROM users
JOIN friendships ON users.id = friendships.user_id
WHERE friendships.friend_id = 1;

SELECT COUNT(id) AS
totalFriendships FROM friendships;

SELECT COUNT(user_id) AS friendCount 
FROM friendships
GROUP BY user_id
HAVING COUNT(user_id) > 1
LIMIT 1;

SELECT user2.first_name, user2.last_name
FROM users 
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id
WHERE friendships.user_id = 3
ORDER BY user2.first_name ASC;

