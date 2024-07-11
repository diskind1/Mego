document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');

    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/dashboard';
                } else {
                    alert(data.message || 'שם משתמש או סיסמה שגויים');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('אירעה שגיאה בהתחברות. אנא נסה שוב מאוחר יותר.');
            });
        });
    }
});