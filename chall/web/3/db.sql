DROP TABLE IF EXISTS user;

DROP TABLE IF EXISTS session;

CREATE TABLE
    user (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        description TEXT NOT NULL
    );

CREATE TABLE
    session (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user (id)
    );

CREATE INDEX idx_username ON user (username);

CREATE INDEX idx_session_id ON session (session_id);

INSERT INTO
    user (username, password, description)
VALUES
    (
        "admin",
        "PlYarElqC3Bo",
        "Welcome back, admin. Here is your flag: web{szNIF6b68zCpInkMhaL4Swmw}"
    ),
    ("user", "LS3IHuQUua6N", "Welcome back, user.");
