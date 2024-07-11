document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM loaded in return_book.js");

    // טעינת מערך הספרים מ-localStorage
    let books = JSON.parse(localStorage.getItem('books'));
    if (!books) {
        console.error("No books found in localStorage");
        alert("שגיאה בטעינת נתוני הספרים.");
        return;
    }

    document.getElementById('returnBook').addEventListener('click', function() {
        const returnSku = document.getElementById('returnSkuInput').value;
        console.log("Attempting to return book with SKU:", returnSku);

        const bookIndex = books.findIndex(b => b.sku === returnSku);
        
        if (bookIndex !== -1) {
            books[bookIndex].quantity++;
            books[bookIndex].available = true;
            console.log("Book returned successfully. New quantity:", books[bookIndex].quantity);
            
            // עדכון ה-localStorage עם המערך המעודכן
            localStorage.setItem('books', JSON.stringify(books));
            
            alert('הספר הוחזר בהצלחה! הכמות החדשה היא: ' + books[bookIndex].quantity);
            document.getElementById('returnSkuInput').value = '';
        } else {
            console.log("Book not found with SKU:", returnSku);
            alert('מק"ט לא נמצא. אנא בדוק שוב.');
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