SELECT tags.id, tags.name
FROM tags
JOIN posts_tags ON posts_tags.tag_id = tags.id
JOIN posts ON posts_tags.post_id = posts.id
WHERE posts.id = 2;

INSERT INTO posts (title) VALUES ('My amazing post');

INSERT INTO tags (name) VALUES ('poetry');

INSERT INTO posts_tags (post_id, tag_id) VALUES (8,5);

SELECT posts.id, posts.title
FROM posts
JOIN posts_tags ON posts_tags.post_id = posts.id
JOIN tags ON posts_tags.tag_id = tags.id
WHERE tags.id = 2;

INSERT INTO posts (title) VALUES ('SQL basics');

INSERT INTO tags (name) VALUES ('sql');

INSERT INTO posts_tags (post_id, tag_id) VALUES (9,6);

SELECT posts.id, posts.title
FROM posts
JOIN posts_tags ON posts_tags.post_id = posts.id
JOIN tags ON posts_tags.tag_id = tags.id
WHERE tags.id = 6;