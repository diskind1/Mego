document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const genreFilter = document.getElementById('genreFilter');
    const skuInput = document.getElementById('skuInput');
    const bookList = document.getElementById('bookList');

    function displayBooks(books) {
        bookList.innerHTML = '';
        books.forEach(book => {
            const li = document.createElement('li');
            li.innerHTML = `
                <strong>${book.title}</strong> מאת ${book.author} (${book.genre})<br>
                מק"ט: ${book.sku} | כמות במלאי: ${book.quantity}
                ${book.quantity > 0 ? 
                    `<button onclick="borrowBook('${book.sku}')">השאל ספר</button>` : 
                    '<span class="unavailable">לא זמין</span>'}
            `;
            if (book.quantity === 0) {
                li.classList.add('unavailable');
            }
            bookList.appendChild(li);
        });
    }

    function filterBooks() {
        const searchTerm = searchInput.value.toLowerCase();
        const selectedGenre = genreFilter.value;

        fetch(`/api/search_books?query=${searchTerm}&genre=${selectedGenre}`)
            .then(response => response.json())
            .then(data => {
                displayBooks(data.books);
            })
            .catch(error => {
                console.error('Error:', error);
                alert('אירעה שגיאה בחיפוש הספרים');
            });
    }

    function searchBySKU() {
        const sku = skuInput.value;
        
        fetch(`/api/search_book_by_sku?sku=${sku}`)
            .then(response => response.json())
            .then(data => {
                if (data.book) {
                    displayBooks([data.book]);
                } else {
                    alert('לא נמצא ספר עם המק"ט הזה');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('אירעה שגיאה בחיפוש הספר');
            });
    }

    if (searchInput) {
        searchInput.addEventListener('input', filterBooks);
    }

    if (genreFilter) {
        genreFilter.addEventListener('change', filterBooks);
    }

    if (skuInput) {
        const searchButton = document.querySelector('button[onclick="searchBySKU()"]');
        if (searchButton) {
            searchButton.addEventListener('click', searchBySKU);
        }
    }

    // טעינה ראשונית של הספרים
    filterBooks();
});

function borrowBook(sku) {
    fetch('/api/borrow_book', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ sku: sku })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('הספר הושאל בהצלחה!');
            filterBooks(); // רענון רשימת הספרים
        } else {
            alert('אירעה שגיאה בהשאלת הספר: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('אירעה שגיאה בהשאלת הספר');
    });
}