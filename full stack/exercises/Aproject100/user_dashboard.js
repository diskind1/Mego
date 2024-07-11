document.addEventListener('DOMContentLoaded', function() {
    const userNameElement = document.getElementById('userName');
    const logoutBtn = document.getElementById('logoutBtn');

    // בדיקה אם המשתמש מחובר
    fetch('/check_login')
        .then(response => response.json())
        .then(data => {
            if (data.logged_in) {
                if (userNameElement) {
                    userNameElement.textContent = `שלום, ${data.username}`;
                }
            } else {
                // אם המשתמש לא מחובר, נעביר אותו לדף ההתחברות
                window.location.href = '/login';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('אירעה שגיאה בטעינת פרטי המשתמש');
        });

    // טיפול בלחיצה על כפתור ההתנתקות
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function() {
            fetch('/logout', { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        window.location.href = '/';
                    } else {
                        alert('אירעה שגיאה בהתנתקות');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('אירעה שגיאה בהתנתקות');
                });
        });
    }
});