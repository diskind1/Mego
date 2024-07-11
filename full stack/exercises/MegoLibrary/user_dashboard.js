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


