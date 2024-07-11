document.addEventListener('DOMContentLoaded', function() {
    const returnSkuInput = document.getElementById('returnSkuInput');
    const returnBookBtn = document.getElementById('returnBook');

    if (returnBookBtn) {
        returnBookBtn.addEventListener('click', function() {
            const sku = returnSkuInput.value;
            if (!sku) {
                alert('אנא הכנס מק"ט להחזרה');
                return;
            }

            fetch('/api/return_book', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ sku: sku })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('הספר הוחזר בהצלחה! הכמות החדשה היא: ' + data.newQuantity);
                    returnSkuInput.value = '';
                } else {
                    alert('אירעה שגיאה בהחזרת הספר: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('אירעה שגיאה בהחזרת הספר.');
            });
        });
    }
});