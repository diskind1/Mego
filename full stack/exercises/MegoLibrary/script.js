document.addEventListener('DOMContentLoaded', function() {
    const loginBtn = document.getElementById('loginBtn');
    const loginOptions = document.querySelector('.login-options');
    const signupLink = document.getElementById('signupLink');
    const signinLink = document.getElementById('signinLink');

    loginBtn.addEventListener('click', function() {
        loginOptions.style.display = loginOptions.style.display === 'block' ? 'none' : 'block';
    });

    signupLink.addEventListener('click', function(e) {
        e.preventDefault();
        // כאן תוכל להוסיף קוד שמפנה לדף ההרשמה (קובץ SQL)
        console.log('מעבר לדף הרשמה');
    });

    signinLink.addEventListener('click', function(e) {
        e.preventDefault();
        // כאן תוכל להוסיף קוד שמפנה לדף ההתחברות
        window.location.href = 'login.html';
    });
});


signupLink.addEventListener('click', function(e) {
    // e.preventDefault(); // מחק או הערה את השורה הזו
    console.log('מעבר לדף הרשמה');
    window.location.href = 'register.html';
});


signupLink.addEventListener('click', function(e) {
    e.preventDefault();
    console.log('מעבר לדף הרשמה');
    // בצע כאן פעולות נוספות אם נדרש
    setTimeout(() => {
        window.location.href = 'register.html';
    }, 100); // מעבר לדף ההרשמה אחרי 100 מילישניות
});

