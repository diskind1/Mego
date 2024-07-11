document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('createAccountForm');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirmPassword').value;

        if (password !== confirmPassword) {
            alert('הסיסמאות אינן תואמות. אנא נסה שנית.');
            return;
        }

        // קבלת נתוני המשתמש מ-localStorage
        let userData = JSON.parse(localStorage.getItem('userData')) || {};

        // הוספת שם משתמש וסיסמה לנתוני המשתמש
        userData.username = username;
        userData.password = password; // בפרויקט אמיתי, יש להצפין את הסיסמה!

        // שמירת הנתונים המעודכנים ב-localStorage
        localStorage.setItem('userData', JSON.stringify(userData));

        alert('החשבון נוצר בהצלחה!');
        window.location.href = 'login.html';
    });
});