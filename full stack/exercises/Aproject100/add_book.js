document.addEventListener('DOMContentLoaded', function() {
    const addBookForm = document.getElementById('addBookForm');

    if (addBookForm) {
        addBookForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const formData = new FormData(addBookForm);
            const bookData = Object.fromEntries(formData.entries());

            fetch('/api/add_book', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(bookData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('הספר נוסף בהצלחה!');
                    addBookForm.reset();
                } else {
                    alert('אירעה שגיאה בהוספת הספר: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('אירעה שגיאה בהוספת הספר.');
            });
        });
    }
});