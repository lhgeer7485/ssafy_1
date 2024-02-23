CREATE TABLE article(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  userid INTEGER NOT NULL, FOREIGN KEY(userid) REFERENCES user(id)
);

CREATE TABLE user(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username VARCHAR(30) NOT NULL UNIQUE,
  email VARCHAR(30) UNIQUE
);

INSERT INTO user (username, email) 
  VALUES 
    ('홍길동', 'hong@email.com'),
    ('이순신', 'lee@email.com'),
    ('유관순', 'ryu@email.com');

CREATE TABLE users(
  PK INTEGER PRIMARY KEY AUTOINCREMENT, 
  email TEXT NOT NULL UNIQUE, 
  name TEXT NOT NULL, 
  age INTEGER NOT NULL,
  phoneNumber TEXT NOT NULL,
  gender INTEGER,
  address TEXT NOT NULL DEFAULT 'no address'
  );

ALTER TABLE users RENAME COLUMN phoneNumber TO number;

DROP TABLE users;

DROP TABLE article;

INSERT INTO article (id, title, content) VALUES (1, '안녕', '이거 들어가나요?');
INSERT INTO article (title, content) VALUES ('안녕', '이거 들어가나요?');

ALTER TABLE article ADD COLUMN created_at DATE NOT NULL DEFAULT '';

ALTER TABLE article RENAME COLUMN content TO contents;

ALTER TABLE article DROP COLUMN created_at;

UPDATE article SET created_at = DATE();

UPDATE article SET created_at = '1900-01-01' WHERE id = 1;

UPDATE article SET title = 'updated title', content = 'new content', created_at = '2023-10-09' WHERE id = 1;

DELETE FROM article WHERE id = 1;

SELECT * FROM article WHERE id = (SELECT id FROM article ORDER BY id ASC LIMIT 2);

SELECT * FROM article WHERE id in (SELECT id FROM article ORDER BY id ASC LIMIT 2);

INSERT INTO article (title, content, userid)
  VALUES
    ('제목2', 'user1이 쓴 글', 1);

DELETE FROM article WHERE userid NOT IN (SELECT id FROM user);