document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM loaded in borrow_book.js");
    const borrowingSku = sessionStorage.getItem('borrowingSku');
    console.log("borrowingSku:", borrowingSku);

    if (!borrowingSku) {
        console.log("No borrowingSku found in sessionStorage");
        document.getElementById('bookDetails').textContent = 'לא נבחר ספר להשאלה.';
        return;
    }

    // טעינת מערך הספרים מ-localStorage
    let books = JSON.parse(localStorage.getItem('books'));
    if (!books) {
        console.error("No books found in localStorage");
        document.getElementById('bookDetails').textContent = 'שגיאה בטעינת נתוני הספרים.';
        return;
    }

    const book = books.find(b => b.sku === borrowingSku);
    console.log("Found book:", book);

    if (!book) {
        document.getElementById('bookDetails').textContent = 'הספר לא נמצא.';
        return;
    }

    document.getElementById('bookDetails').innerHTML = `
        <h3>${book.title}</h3>
        <p>מאת: ${book.author}</p>
        <p>ז'אנר: ${book.genre}</p>
        <p>מק"ט: ${book.sku}</p>
        <p>כמות זמינה: ${book.quantity}</p>
    `;

    document.getElementById('confirmBorrow').addEventListener('click', function() {
        console.log("Confirm button clicked");
        if (book.quantity > 0) {
            book.quantity--;
            book.available = book.quantity > 0;
            
            // עדכון ה-localStorage עם המערך המעודכן
            localStorage.setItem('books', JSON.stringify(books));
            
            console.log("Book borrowed successfully. New quantity:", book.quantity);
            alert(`הספר הושאל בהצלחה! הכמות החדשה היא: ${book.quantity}`);
            sessionStorage.removeItem('borrowingSku');
            window.location.href = 'index.html';
        } else {
            alert('מצטערים, הספר אינו זמין כרגע.');
        }
    });
});







document.addEventListener('DOMContentLoaded', function() {
    // בדיקה אם המשתמש מחובר (לדוגמה, באמצעות sessionStorage)
    const userName = sessionStorage.getItem('userName');
    if (!userName) {
        // אם המשתמש לא מחובר, נעביר אותו לדף ההתחברות
        window.location.href = 'login.html';
    } else {
        // עדכון שם המשתמש בעמוד
        document.getElementById('userName').textContent += userName;
    }

    // טיפול בלחיצה על כפתור ההתנתקות
    document.getElementById('logoutBtn').addEventListener('click', function() {
        sessionStorage.removeItem('userName');
        window.location.href = 'index.html';
    });
});



