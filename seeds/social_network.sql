DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text
);

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  views int,
-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id) 
    on delete cascade
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, email) VALUES ('kezzy1', 'k1@email.com');
INSERT INTO users (username, email) VALUES ('kezzy2', 'k2@email.com');
INSERT INTO users (username, email) VALUES ('kezzy3', 'k3@email.com');
INSERT INTO users (username, email) VALUES ('kezzy4', 'k4@email.com');

INSERT INTO posts (title, content, views, user_id) VALUES ('New job1','WOOO I have a new job1!', 0, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('New job2','WOOO I have a new job2!', 10, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('New job3','WOOO I have a new job3!', 20, 3);
INSERT INTO posts (title, content, views, user_id) VALUES ('New job4','WOOO I have a new job4!', 30, 4);