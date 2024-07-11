document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registrationForm');
    const paymentMethod = document.getElementById('paymentMethod');
    const creditCardDetails = document.getElementById('creditCardDetails');
    const debitDetails = document.getElementById('debitDetails');

    paymentMethod.addEventListener('change', function() {
        if (this.value === 'credit') {
            creditCardDetails.style.display = 'block';
            debitDetails.style.display = 'none';
        } else if (this.value === 'debit') {
            creditCardDetails.style.display = 'none';
            debitDetails.style.display = 'block';
        } else {
            creditCardDetails.style.display = 'none';
            debitDetails.style.display = 'none';
        }
    });

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // שמירת נתוני המשתמש ב-localStorage
        const userData = {
            firstName: document.getElementById('firstName').value,
            lastName: document.getElementById('lastName').value,
            idNumber: document.getElementById('idNumber').value,
            email: document.getElementById('email').value,
            phone: document.getElementById('phone').value,
            paymentMethod: paymentMethod.value
        };
        
        localStorage.setItem('userData', JSON.stringify(userData));
        
        // מעבר לדף יצירת שם משתמש וסיסמה
        window.location.href = 'create_account.html';
    });
});