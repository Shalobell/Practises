import sqlite3
import os

from db import init_db

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_DIR = os.path.join(BASE_DIR, "db")
DB_PATH = os.path.join(DB_DIR, "shop.db")

os.makedirs(DB_DIR, exist_ok=True)


def get_connection():
    return sqlite3.connect(DB_PATH)


def add_product():
    title = input("Название товара: ").strip()
    if not title:
        print("Название не может быть пустым.")
        return
    try:
        price = float(input("Цена (руб.): ").strip())
        if price <= 0:
            raise ValueError
    except ValueError:
        print("Некорректная цена.")
        return
    try:
        quantity = int(input("Количество на складе: ").strip())
        if quantity < 0:
            raise ValueError
    except ValueError:
        print("Некорректное количество.")
        return

    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO products (title, price, quantity) VALUES (?, ?, ?)",
                (title, price, quantity)
            )
            conn.commit()
            print(f"Товар '{title}' добавлен (ID: {cur.lastrowid})")
    except sqlite3.IntegrityError as e:
        if "UNIQUE" in str(e):
            print("Товар с таким названием уже существует.")
        else:
            print(f"Ошибка БД: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")


def register_customer():
    fio = input("ФИО: ").strip()
    phone = input("Телефон (например, +79991234567): ").strip()
    email = input("Email (опционально): ").strip() or None

    if not fio or not phone:
        print("ФИО и телефон обязательны.")
        return

    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO customers (fio, phone, email) VALUES (?, ?, ?)",
                (fio, phone, email)
            )
            conn.commit()
            print(f"Покупатель '{fio}' зарегистрирован (ID: {cur.lastrowid})")
    except sqlite3.IntegrityError:
        print("Покупатель с таким телефоном уже зарегистрирован.")
    except Exception as e:
        print(f"Ошибка: {e}")


def create_order():
    print("\n--- Выбор покупателя ---")
    phone = input("Введите телефон покупателя (или 'new' для регистрации): ").strip()

    customer_id = None
    if phone.lower() == 'new':
        register_customer()
        return
    else:
        try:
            with get_connection() as conn:
                cur = conn.cursor()
                cur.execute("SELECT id, fio FROM customers WHERE phone = ?", (phone,))
                customer = cur.fetchone()
                if not customer:
                    print("Покупатель не найден. Сначала зарегистрируйте его.")
                    return
                customer_id, fio = customer
                print(f"Выбран покупатель: {fio} (ID: {customer_id})")
        except Exception as e:
            print(f"Ошибка поиска покупателя: {e}")
            return

    print("\n--- Добавление товаров в заказ ---")
    print("Введите ID товара и количество. Для завершения введите 'готово'.")

    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, title, price, quantity FROM products WHERE quantity > 0 ORDER BY title")
            products = cur.fetchall()
            if not products:
                print("Нет товаров в наличии!")
                return
            print("\nДоступные товары:")
            print(f"{'ID':<4} {'Название':<25} {'Цена':<8} {'Остаток'}")
            print("-" * 50)
            for p in products:
                print(f"{p[0]:<4} {p[1]:<25} {p[2]:<8.2f} {p[3]}")
    except Exception as e:
        print(f"Ошибка загрузки товаров: {e}")
        return

    order_items = []
    while True:
        line = input("\n>ID и количество (например: 3 2) или 'готово': ").strip()
        if line.lower() == 'готово':
            break
        parts = line.split()
        if len(parts) != 2:
            print("Формат: <ID> <количество>")
            continue
        try:
            product_id = int(parts[0])
            qty = int(parts[1])
            if qty <= 0:
                print("Количество должно быть > 0")
                continue
        except ValueError:
            print("ID и количество — целые числа")
            continue

        try:
            with get_connection() as conn:
                cur = conn.cursor()
                cur.execute("SELECT title, price, quantity FROM products WHERE id = ?", (product_id,))
                prod = cur.fetchone()
                if not prod:
                    print(f"Товар с ID {product_id} не найден")
                    continue
                title, price, stock = prod
                if qty > stock:
                    print(f"Недостаточно товара '{title}': в наличии {stock}, запрошено {qty}")
                    continue
                order_items.append((product_id, qty, price, title))
                print(f"Добавлено: {title} ×{qty}")
        except Exception as e:
            print(f"Ошибка проверки товара: {e}")
            continue

    if not order_items:
        print("Заказ пуст. Отмена.")
        return

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("BEGIN IMMEDIATE")

        cur.execute("INSERT INTO orders (customer_id) VALUES (?)", (customer_id,))
        order_id = cur.lastrowid
        print(f"\nСоздан заказ №{order_id}")

        total_sum = 0.0

        for product_id, qty, price, title in order_items:
            cur.execute("""
                UPDATE products 
                SET quantity = quantity - ? 
                WHERE id = ? AND quantity >= ?
            """, (qty, product_id, qty))

            if cur.rowcount == 0:
                conn.rollback()
                conn.close()
                raise Exception(f"Недостаточно товара '{title}' при оформлении (остаток изменился). Заказ отменён.")

            cur.execute("""
                INSERT INTO order_items (order_id, product_id, quantity, price_at_purchase)
                VALUES (?, ?, ?, ?)
            """, (order_id, product_id, qty, price))

            total_sum += qty * price

        conn.commit()
        conn.close()
        print(f"Заказ №{order_id} успешно оформлен!")
        print(f"Итого: {total_sum:.2f} руб.")

    except Exception as e:
        try:
            if conn:
                conn.rollback()
                conn.close()
        except:
            pass
        print(f"Ошибка при оформлении заказа: {e}")


def show_all_orders():
    print("\n--- Все заказы с детализацией ---")
    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute('''
                SELECT 
                    o.id,
                    c.fio,
                    o.order_date,
                    SUM(oi.quantity * oi.price_at_purchase) AS total
                FROM orders o
                JOIN customers c ON o.customer_id = c.id
                JOIN order_items oi ON oi.order_id = o.id
                GROUP BY o.id, c.fio, o.order_date
                ORDER BY o.order_date DESC
            ''')
            orders = cur.fetchall()

            if not orders:
                print("Нет оформленных заказов.")
                return

            for order_id, fio, date_str, total in orders:
                print(f"\nЗаказ №{order_id} от {date_str}")
                print(f"   Покупатель: {fio}")
                print(f"   Сумма: {total:.2f} руб.")
                print("   Товары:")

                cur.execute('''
                    SELECT p.title, oi.quantity, oi.price_at_purchase
                    FROM order_items oi
                    JOIN products p ON oi.product_id = p.id
                    WHERE oi.order_id = ?
                ''', (order_id,))
                items = cur.fetchall()
                for title, qty, price in items:
                    print(f"{title} ×{qty} @ {price:.2f} = {qty * price:.2f} руб.")

    except Exception as e:
        print(f"Ошибка загрузки заказов: {e}")


def show_top5_popular():
    print("\n--- Топ-5 самых популярных товаров (по количеству проданных штук) ---")
    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute('''
                SELECT 
                    p.title,
                    SUM(oi.quantity) AS total_sold
                FROM order_items oi
                JOIN products p ON oi.product_id = p.id
                GROUP BY p.id, p.title
                ORDER BY total_sold DESC
                LIMIT 5
            ''')
            rows = cur.fetchall()

            if not rows:
                print("Пока нет продаж.")
                return

            print(f"{'Место':<6} {'Товар':<30} {'Продано, шт'}")
            print("-" * 45)
            for i, (title, total) in enumerate(rows, 1):
                print(f"{i:<6} {title:<30} {int(total)}")

    except Exception as e:
        print(f"Ошибка загрузки ТОП-5: {e}")


def main_menu():
    init_db_if_needed()
    while True:
        print("\n" + "=" * 50)
        print("СИСТЕМА УПРАВЛЕНИЯ МАГАЗИНОМ")
        print("=" * 50)
        print("1. Добавить товар")
        print("2. Зарегистрировать покупателя")
        print("3. Оформить заказ")
        print("4. Показать все заказы")
        print("5. ТОП-5 популярных товаров")
        print("0. Выйти")
        choice = input("\nВыберите действие: ").strip()

        if choice == '1':
            add_product()
        elif choice == '2':
            register_customer()
        elif choice == '3':
            create_order()
        elif choice == '4':
            show_all_orders()
        elif choice == '5':
            show_top5_popular()
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def init_db_if_needed():
    if not os.path.exists(DB_PATH):
        init_db(DB_PATH)
    else:
        try:
            with get_connection() as conn:
                cur = conn.cursor()
                cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
                if not cur.fetchone():
                    print("Таблицы отсутствуют — инициализируем БД...")
                    init_db(DB_PATH)
        except Exception as e:
            print(f"Ошибка проверки БД: {e}. Попытка инициализации...")
            init_db(DB_PATH)


if __name__ == "__main__":
    main_menu()