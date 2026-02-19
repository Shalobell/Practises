import sqlite3


def init_db(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Таблица товаров
    cur.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            price REAL NOT NULL CHECK(price > 0),
            quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0)
        )
    ''')

    # Таблица покупателей
    cur.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fio TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            email TEXT
        )
    ''')

    # Таблица заказов
    cur.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE CASCADE
        )
    ''')

    # Таблица позиций заказа
    cur.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity > 0),
            price_at_purchase REAL NOT NULL,
            PRIMARY KEY (order_id, product_id),
            FOREIGN KEY(order_id) REFERENCES orders(id) ON DELETE CASCADE,
            FOREIGN KEY(product_id) REFERENCES products(id) ON DELETE RESTRICT
        )
    ''')

    conn.commit()
    print("База данных инициализирована.")

    cur.execute("SELECT COUNT(*) FROM products")
    if cur.fetchone()[0] == 0:
        print("Добавляем демо-товары...")
        demo_products = [
            ("Товар 1", 1000.0, 1),
            ("Товар 2", 2000.0, 2),
            ("Товар 3", 3000.0, 3),
            ("Товар 4", 4000.0, 4),
            ("Товар 5", 5000.0, 5),
        ]
        cur.executemany(
            "INSERT INTO products (title, price, quantity) VALUES (?, ?, ?)",
            demo_products
        )
        print("5 товаров добавлено.")

    cur.execute("SELECT COUNT(*) FROM customers")
    if cur.fetchone()[0] == 0:
        print("Добавляем демо-покупателей...")
        demo_customers = [
            ("Пользователь 1", "+12345678901", "user1@example.com"),
            ("Пользователь 2", "+12345678902", "user2@example.com"),
            ("Пользователь 3", "+12345678903", None),
            ("Пользователь 4", "+12345678904", "user4@example.com")
        ]
        cur.executemany(
            "INSERT INTO customers (fio, phone, email) VALUES (?, ?, ?)",
            demo_customers
        )
        print("4 покупателя добавлено.")

    conn.commit()
    conn.close()