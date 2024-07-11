document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // כאן תוכל להוסיף את הלוגיקה לבדיקת פרטי ההתחברות
        console.log('ניסיון התחברות עם:', username, password);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // כאן בדרך כלל תבצע בדיקה מול השרת
        // לצורך הדוגמה, נניח שההתחברות הצליחה
        console.log('ניסיון התחברות עם:', username, password);

        // שמירת שם המשתמש ב-sessionStorage
        sessionStorage.setItem('userName', username);

        // העברה לדף הראשי
        window.location.href = 'user_dashboard.html';
    });
});






document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // בדיקה מול ה-sessionStorage
        const storedUsername = sessionStorage.getItem('userName');
        const storedPassword = sessionStorage.getItem('userPassword');

        if (username === storedUsername && password === storedPassword) {
            console.log('התחברות מוצלחת');
            window.location.href = 'user_dashboard.html';
        } else {
            alert('שם משתמש או סיסמה שגויים');
        }
    });
});