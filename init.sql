CREATE TABLE news (
    uid         INTEGER       PRIMARY KEY AUTOINCREMENT,
    id          INTEGER,
    keywords    VARCHAR (100),
    description VARCHAR (500),
    url         VARCHAR (200),
    title       VARCHAR (100),
    source      VARCHAR (20),
    content     VARCHAR (500),
    author      VARCHAR (10) 
);