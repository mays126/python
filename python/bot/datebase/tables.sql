CREATE TABLE IF NOT EXISTS menu(
    name TEXT NOT NULL PRIMARY KEY,
    photo TEXT NOT NULL,
    type TEXT NOT NULL,
    price INTEGER NOT NULL,
    ingridients TEXT NOT NULL
);





CREATE TABLE IF NOT EXISTS rolls(
    id INTEGER PRIMARY KEY,
    photo TEXT NOT NULL,
    username TEXT NOT NULL,
    userpass TEXT NOT NULL,
    adress TEXT NOT NULL,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    ingridients TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pizzas(
    id INTEGER PRIMARY KEY,
    photo TEXT NOT NULL,
    username TEXT NOT NULL,
    userpass TEXT NOT NULL,
    adress TEXT NOT NULL,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    ingridients TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS burgers(
    id INTEGER PRIMARY KEY,
    photo TEXT NOT NULL,
    username TEXT NOT NULL,
    userpass TEXT NOT NULL,
    adress TEXT NOT NULL,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    ingridients TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS accaunts(
    username TEXT NOT NULL PRIMARY KEY,
    userpass TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS admins(
    adminname TEXT NOT NULL PRIMARY KEY,
    adminpass TEXT NOT NULL
);