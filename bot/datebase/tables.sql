CREATE TABLE IF NOT EXISTS done_homework(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    photo TEXT NULL,
    username TEXT NOT NULL,
    userpass TEXT NOT NULL,
    adminname TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS check_homework(
    id INTEGER PRIMARY KEY AUTOINCRIMENT,
    photo TEXT NULL,
    username TEXT NOT NULL,
    userpass TEXT NOT NULL,
    adminname TEXT NOT NULL,
    adminpass TEXT NOT NULL,
    mark INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS homework(
    id INTEGER PRIMARY KEY AUTOINCRIMENT,
    name TEXT NOT NULL,
    photo TEXT NULL,
);

CREATE TABLE IF NOT EXISTS accaunts(
    username TEXT NOT NULL PRIMARY KEY,
    userpass TEXT NOT NULL,
);

CREATE TABLE IF NOT EXISTS admins(
    adminname TEXT NOT NULL PRIMARY KEY,
    adminpass TEXT NOT NULL,
);