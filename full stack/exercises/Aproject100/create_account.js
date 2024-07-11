document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('createAccountForm');

    if (form) {
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

            // שליחת הנתונים לשרת
            fetch('/create_account', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(userData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('החשבון נוצר בהצלחה!');
                    localStorage.removeItem('userData'); // מחיקת הנתונים מהאחסון המקומי
                    window.location.href = '/login';
                } else {
                    alert('יצירת החשבון נכשלה: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('אירעה שגיאה ביצירת החשבון. אנא נסה שנית מאוחר יותר.');
            });
        });
    }
});