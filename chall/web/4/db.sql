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
    ("user", "WvA8lMUiHo0e", "Welcome back, user."),
    (
        "user_Gi0veh7U",
        "ArxWyWR9kpBi",
        "Welcome back, user."
    ),
    (
        "user_ohX7po1t",
        "6vWozrAgcCis",
        "Welcome back, user."
    ),
    (
        "user_toh5Ebee",
        "s1oe49pvNMQo",
        "Welcome back, user."
    ),
    (
        "user_soh0Rah8",
        "jKy66OZV9Aip",
        "Welcome back, user."
    ),
    (
        "user_pak0Thah",
        "2VvP84sskiSB",
        "Welcome back, user. Here is your flag: web{67rFlAjZoT2ilklESiyuBmFr}"
    ),
    (
        "user_hae8Thoh",
        "UrcoBujI6FaJ",
        "Welcome back, user."
    ),
    (
        "user_ViT7Kei8",
        "Vv4l043cAMcZ",
        "Welcome back, user."
    ),
    (
        "user_iePhie8a",
        "bf7OeFwpL9Bs",
        "Welcome back, user."
    ),
    (
        "user_Cuv1ie8o",
        "SWf9qR0qMTmB",
        "Welcome back, user."
    ),
    (
        "user_fai3zooT",
        "oFEg0HlVnVoW",
        "Welcome back, user."
    );
