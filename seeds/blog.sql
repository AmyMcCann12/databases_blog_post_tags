DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text
);

CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content text,
    author text,

    post_id int,
    constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, content) VALUES ('Title1', 'Contents1');
INSERT INTO posts (title, content) VALUES ('Title2', 'Contents2');
INSERT INTO posts (title, content) VALUES ('Title3', 'Contents3');
INSERT INTO posts (title, content) VALUES ('Title4', 'Contents4');
INSERT INTO posts (title, content) VALUES ('Title5', 'Contents5');


INSERT INTO comments (content, author, post_id) VALUES ('Comments content 1', 'Author1', 1);
INSERT INTO comments (content, author, post_id) VALUES ('Comments content 2', 'Author2', 2);
INSERT INTO comments (content, author, post_id) VALUES ('Comments content 3', 'Author3', 2);
INSERT INTO comments (content, author, post_id) VALUES ('Comments content 4', 'Author4', 3);
INSERT INTO comments (content, author, post_id) VALUES ('Comments content 5', 'Author5', 4);
INSERT INTO comments (content, author, post_id) VALUES ('Comments content 6', 'Author6', 5);
INSERT INTO comments (content, author, post_id) VALUES ('Comments content 7', 'Author7', 4);
INSERT INTO comments (content, author, post_id) VALUES ('Comments content 8', 'Author8', 3);