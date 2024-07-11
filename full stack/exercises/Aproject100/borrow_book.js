document.addEventListener('DOMContentLoaded', function() {
    const bookDetails = document.getElementById('bookDetails');
    const confirmBorrowBtn = document.getElementById('confirmBorrow');

    function loadBookDetails() {
        const urlParams = new URLSearchParams(window.location.search);
        const bookId = urlParams.get('book_id');

        if (bookId) {
            fetch(`/api/book_details/${bookId}`)
                .then(response => response.json())
                .then(data => {
                    if (data.book) {
                        bookDetails.innerHTML = `
                            <h3>${data.book.title}</h3>
                            <p>מאת: ${data.book.author}</p>
                            <p>ז'אנר: ${data.book.genre}</p>
                            <p>מק"ט: ${data.book.sku}</p>
                            <p>כמות זמינה: ${data.book.quantity}</p>
                        `;
                        confirmBorrowBtn.style.display = 'block';
                    } else {
                        bookDetails.textContent = 'הספר לא נמצא.';
                        confirmBorrowBtn.style.display = 'none';
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    bookDetails.textContent = 'אירעה שגיאה בטעינת פרטי הספר.';
                    confirmBorrowBtn.style.display = 'none';
                });
        } else {
            bookDetails.textContent = 'לא נבחר ספר להשאלה.';
            confirmBorrowBtn.style.display = 'none';
        }
    }

    if (confirmBorrowBtn) {
        confirmBorrowBtn.addEventListener('click', function() {
            const urlParams = new URLSearchParams(window.location.search);
            const bookId = urlParams.get('book_id');

            fetch('/api/borrow_book', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ book_id: bookId })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('הספר הושאל בהצלחה!');
                    window.location.href = '/dashboard';
                } else {
                    alert('אירעה שגיאה בהשאלת הספר: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('אירעה שגיאה בהשאלת הספר.');
            });
        });
    }

    loadBookDetails();
});