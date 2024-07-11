import os
import sys
from flask import Flask, render_template, request, redirect, url_for, flash, session
from database_operations import *
from functools import wraps

print("Python version:", sys.version)
print("Current working directory:", os.getcwd())
print("Content of current directory:", os.listdir())

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # החלף זאת במפתח אמיתי וסודי

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('עליך להתחבר כדי לגשת לדף זה', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def librarian_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session or not session.get('is_librarian'):
            flash('אין לך הרשאה לגשת לדף זה', 'error')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = authenticate_user(username, password)
        if user:
            session['user_id'] = user['id']
            session['is_librarian'] = user['is_librarian']
            flash('התחברת בהצלחה!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('שם משתמש או סיסמה שגויים', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash('התנתקת בהצלחה', 'success')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if add_user(username, password):
            flash('נרשמת בהצלחה! אנא התחבר.', 'success')
            return redirect(url_for('login'))
        else:
            flash('הרשמה נכשלה. אנא נסה שנית.', 'error')
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    if session.get('is_librarian'):
        return render_template('librarian_dashboard.html')
    else:
        return render_template('user_dashboard.html')

@app.route('/books')
@login_required
def books():
    all_books = get_all_books()
    return render_template('books.html', books=all_books)

@app.route('/add_book', methods=['GET', 'POST'])
@librarian_required
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        sku = request.form['sku']
        quantity = int(request.form['quantity'])
        add_book(title, author, genre, sku, quantity)
        flash('הספר נוסף בהצלחה!', 'success')
        return redirect(url_for('books'))
    return render_template('add_book.html')

@app.route('/update_book/<int:book_id>', methods=['GET', 'POST'])
@librarian_required
def update_book(book_id):
    book = get_book_by_id(book_id)
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        sku = request.form['sku']
        quantity = int(request.form['quantity'])
        if update_book_in_db(book_id, title, author, genre, sku, quantity):
            flash('הספר עודכן בהצלחה!', 'success')
            return redirect(url_for('books'))
        else:
            flash('עדכון הספר נכשל. אנא נסה שנית.', 'error')
    return render_template('update_book.html', book=book)

@app.route('/borrow_book')
@login_required
def borrow_book_page():
    return render_template('borrow_book.html')

@app.route('/borrow_book/<int:book_id>', methods=['POST'])
@login_required
def borrow_book(book_id):
    if borrow_book_in_db(session['user_id'], book_id):
        flash('הספר הושאל בהצלחה', 'success')
    else:
        flash('אירעה שגיאה בהשאלת הספר', 'error')
    return redirect(url_for('dashboard'))

@app.route('/return_book')
@login_required
def return_book_page():
    return render_template('return_book.html')

@app.route('/return_book/<int:book_id>', methods=['POST'])
@login_required
def return_book(book_id):
    if return_book_in_db(session['user_id'], book_id):
        flash('הספר הוחזר בהצלחה', 'success')
    else:
        flash('אירעה שגיאה בהחזרת הספר', 'error')
    return redirect(url_for('dashboard'))

@app.route('/search_books')
@login_required
def search_books():
    query = request.args.get('query', '')
    books = search_books_in_db(query)
    return render_template('search_books.html', books=books, query=query)

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if create_account_in_db(username, password, email):
            flash('החשבון נוצר בהצלחה! אנא התחבר.', 'success')
            return redirect(url_for('login'))
        else:
            flash('יצירת החשבון נכשלה. אנא נסה שנית.', 'error')
    return render_template('create_account.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)