import sqlite3

conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()


def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        amount REAL,
        category TEXT,
        note TEXT
    )
    ''')
    conn.commit()


def add_expense(tupl):
    cursor.execute('''
    INSERT INTO expenses (date, amount, category, note)
    VALUES (?, ?, ?, ?)
    ''', tupl)
    conn.commit()


def delete_all_expenses():
    cursor.execute('DELETE FROM expenses')
    cursor.execute('DELETE FROM sqlite_sequence WHERE name="expenses"')
    conn.commit()


def delete_expense(ex_id):

    cursor.execute('DELETE FROM expenses WHERE id = ?', (ex_id,))

    cursor.execute('''
        UPDATE expenses
        SET id = id - 1
        WHERE id > ?
    ''', (ex_id,))

    cursor.execute('DELETE FROM sqlite_sequence WHERE name="expenses"')

    conn.commit()


def edit_expense(ex_id, new_data):
    cursor.execute('''
        UPDATE expenses
        SET date = ?, amount = ?, category = ?, note = ?
        WHERE id = ?
    ''', (*new_data, ex_id))
    conn.commit()


def print_expenses(expenses):
    for row in expenses:
        print(
            f"ID: {row[0]} | Date: {row[1]} | Amount: {row[2]} | Category: {row[3]}")


def show_expense(ex_id):
    cursor.execute('SELECT * FROM expenses WHERE id = ?', (ex_id,))
    row = cursor.fetchone()
    if row:
        print(
            f"ID: {row[0]} | Date: {row[1]} | Amount: {row[2]} | Category: {row[3]} | Note: {row[4]}")
    else:
        print("Expense not found.")


def get_expenses():
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    return rows
