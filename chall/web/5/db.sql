DROP TABLE IF EXISTS user;

DROP TABLE IF EXISTS session;

CREATE TABLE
    menu (
        menu_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        price FLOAT NOT NULL
    );

CREATE TABLE
    flag (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        flag TEXT NOT NULL
    );

INSERT INTO
    flag (name, flag)
VALUES
    (
        "Secret",
        "web{IB9FW5fS1PO2b4DFkZhoDVMN}"
    );

INSERT INTO
    menu (name, description, price)
VALUES
    (
        "Pad Thai",
        "Stir-fried rice noodle dish with shrimp, tofu, and peanuts",
        8.99
    ),
    (
        "Tom Yum Goong",
        "Spicy and sour shrimp soup with lemongrass",
        7.99
    ),
    (
        "Green Curry",
        "Thai green curry with chicken and vegetables",
        9.99
    ),
    (
        "Thai Iced Tea",
        "Sweetened iced tea with milk",
        3.50
    ),
    (
        "Mango Sticky Rice",
        "Sweet sticky rice with fresh mango and coconut milk",
        5.99
    ),
    ("Som Tum", "Spicy green papaya salad", 6.99),
    (
        "Massaman Curry",
        "Rich and creamy curry with beef and potatoes",
        10.99
    ),
    (
        "Chicken Satay",
        "Grilled chicken skewers served with peanut sauce",
        7.50
    ),
    (
        "Spring Rolls",
        "Crispy rolls filled with vegetables and glass noodles",
        4.99
    ),
    (
        "Fried Banana",
        "Deep-fried banana with honey and sesame seeds",
        3.99
    );
