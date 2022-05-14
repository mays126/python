CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY,
    book_name TEXT NOT NULL,
    author TEXT NOT NULL,
    colvo_tomov INTEGER NOT NULL
);


CREATE TABLE IF NOT EXISTS visitors(
    tel_number INTEGER PRIMARY KEY,
    visitor_name TEXT NOT NULL,
    surname TEXT NOT NULL,
    adress TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS registred_books(
    id INTEGER PRIMARY KEY,
    book TEXT NOT NULL,
    visitor INTEGER NOT NULL
);
