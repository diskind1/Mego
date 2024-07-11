import sys
print(sys.path)
import bcrypt
import pyodbc
print("יבוא הספריות הצליח")


import pyodbc
import bcrypt
from datetime import datetime

DB_CONFIG = {
    'driver': '{SQL Server}',
    'server': r'MENNI-OFFICE\SQLEXPRESS',
    'database': 'LibraryDB',
    'trusted_connection': 'yes'
}

def get_db_connection():
    conn_str = ';'.join(f"{k}={v}" for k, v in DB_CONFIG.items())
    try:
        return pyodbc.connect(conn_str)
    except pyodbc.Error as e:
        print(f"שגיאה בהתחברות למסד הנתונים: {e}")
        return None

def db_operation(func):
    def wrapper(*args, **kwargs):
        conn = get_db_connection()
        if not conn:
            return None
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except pyodbc.Error as e:
            print(f"שגיאה בפעולת בסיס הנתונים: {e}")
            conn.rollback()
            return None
        finally:
            conn.close()
    return wrapper

@db_operation
def get_all_books(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    return cursor.fetchall()

@db_operation
def add_book(conn, title, author, genre, sku, quantity):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Books (Title, Author, Genre, SKU, Quantity) VALUES (?, ?, ?, ?, ?)",
                   (title, author, genre, sku, quantity))

@db_operation
def update_book_in_db(conn, book_id, title, author, genre, sku, quantity):
    cursor = conn.cursor()
    cursor.execute("UPDATE Books SET Title=?, Author=?, Genre=?, SKU=?, Quantity=? WHERE BookID=?",
                   (title, author, genre, sku, quantity, book_id))
    return cursor.rowcount > 0

@db_operation
def get_book_by_id(conn, book_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books WHERE BookID = ?", (book_id,))
    return cursor.fetchone()

@db_operation
def borrow_book_in_db(conn, user_id, book_id):
    cursor = conn.cursor()
    cursor.execute("SELECT Quantity FROM Books WHERE BookID = ?", (book_id,))
    book = cursor.fetchone()
    if not book or book.Quantity <= 0:
        return False
    
    cursor.execute("UPDATE Books SET Quantity = Quantity - 1 WHERE BookID = ?", (book_id,))
    cursor.execute("INSERT INTO Loans (UserID, BookID, LoanDate) VALUES (?, ?, ?)",
                   (user_id, book_id, datetime.now()))
    return True

@db_operation
def return_book_in_db(conn, user_id, book_id):
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 1 LoanID FROM Loans WHERE UserID = ? AND BookID = ? AND ReturnDate IS NULL", (user_id, book_id))
    loan = cursor.fetchone()
    if not loan:
        return False
    
    cursor.execute("UPDATE Loans SET ReturnDate = ? WHERE LoanID = ?", (datetime.now(), loan.LoanID))
    cursor.execute("UPDATE Books SET Quantity = Quantity + 1 WHERE BookID = ?", (book_id,))
    return True

@db_operation
def add_user(conn, username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (Username, Password, IsLibrarian) VALUES (?, ?, ?)",
                   (username, hashed_password, False))
    return True

@db_operation
def authenticate_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT UserID, Password, IsLibrarian FROM Users WHERE Username = ?", (username,))
    user = cursor.fetchone()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.Password.encode('utf-8')):
        return {'id': user.UserID, 'is_librarian': user.IsLibrarian}
    return None

@db_operation
def search_books_in_db(conn, query):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books WHERE Title LIKE ? OR Author LIKE ? OR Genre LIKE ?",
                   (f"%{query}%", f"%{query}%", f"%{query}%"))
    return cursor.fetchall()

@db_operation
def create_account_in_db(conn, username, password, email):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (Username, Password, Email, IsLibrarian) VALUES (?, ?, ?, ?)",
                   (username, hashed_password, email, False))
    return True


print("database_operations.py executed successfully")