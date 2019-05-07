-- create db --
CREATE TABLE items (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    name TEXT NOT NULL,
    long_descript TEXT
);

CREATE TABLE histories (
    itemid INTEGER,
    time DATETIME DEFAULT (datetime('now', 'localtime')),
    FOREIGN KEY (itemid) REFERENCES items(id)
);