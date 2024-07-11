



const books = [ 
    { title: "מסע אל תום האלף", author: "א.ב. יהושע", genre: "רומן", available: true, sku: "100001", quantity: 3  },
    { title: "הקוד של דה וינצ'י", author: "דן בראון", genre: "מתח", available: false, sku: "100002", quantity: 0 },
    { title: "1984", author: "ג'ורג' אורוול", genre: "מדע בדיוני", available: true, sku: "100003", quantity: 2  },
    { title: "מלחמה ושלום", author: "לב טולסטוי", genre: "היסטוריה", available: false, sku: "100004", quantity: 0  },
    { title: "המשחק של אנדר", author: "אורסון סקוט קארד", genre: "מדע בדיוני", available: true, sku: "100005", quantity: 7  },
    { title: "האמת ושלום", author: "ישי לב", genre: "", available: true, sku: "100006", quantity: 3  },
    { title: "היו נכונים", author: "ארי טויב", genre: "מתח", available: true, sku: "100007", quantity: 4  },
    { title: "כי אלך", author: "ברכה צדוק", genre: "מתח", available: false, sku: "100008", quantity: 0  },
    { title: "לא לבד", author: "דודי חיים", genre: "רומן", available: true, sku: "100009", quantity: 8  },
    { title: "בשביל האפור", author: "אהרן שליו", genre: "רומן", available: true, sku: "100010", quantity: 2  },
    { title: "זריז נשכר", author: "שמעון הכהן", genre: "קומדיה", available: true, sku: "100011", quantity: 1  },
    { title: "קריית משה", author: "מוטי ליאון", genre: "היסטוריה", available: false, sku: "100012", quantity: 0  },
    { title: "הרכבת עזבה", author: "גיא כספי", genre: "מתח", available: true, sku: "100013", quantity: 2  },
    { title: "בניה חדשה", author: "תמר בת מלך", genre: "רומן", available: true, sku: "100014", quantity: 4  },
    { title: "SCRIPTIM", author: "יוספי ארנשטיין", genre: "קומדיה", available: true, sku: "100015", quantity: 6  },
    { title: "יש כח", author: "ברכה שרמן", genre: "קומדיה", available: true, sku: "100016", quantity: 1  },
    { title: "שלבים", author: "איילת ברים", genre: "מדע בדיוני", available: true, sku: "100017", quantity: 3  },
    { title: "לחפש", author: "חיים צבי", genre: "רומן", available: false, sku: "100018", quantity: 0  },
    { title: "המרגל", author: "אורית דיין", genre: "מדע בדיוני", available: false, sku: "100019", quantity: 0  },
    { title: "דוד ושלמה", author: "ישראל בן חיסדא", genre: "היסטוריה", available: true, sku: "100020", quantity: 3  },
    { title: "גירסה אחרונה", author: "לוי שבליט", genre: "מתח", available: false, sku: "100021", quantity: 0  },
    { title: "בדרך המלך", author: "'צבי רננוביץ", genre: "קומדיה", available: false, sku: "100022", quantity: 0  },
    { title: "לוג אחד", author: "חיים אורלב", genre: "מדע בדיוני", available: true, sku: "100023", quantity: 1  },
    { title: "סתם היו", author: "בן צבי גיטלמן", genre: "קומדיה", available: true, sku: "100024", quantity: 5  },
    { title: "ששון מהכפר", author: "ישי לוי", genre: "קומדיה", available: true, sku: "100025", quantity: 2  },
    { title: "שיר ושבחה", author: "דוד המשורר", genre: "היסטוריה", available: true, sku: "100026", quantity: 2  },
    { title: "שברי אותיות", author: "אביהו בן נעים", genre: "היסטוריה", available: false, sku: "100027", quantity: 0  },
    { title: "חצות", author: ".שיר ג", genre: "רומן", available: true, sku: "100028", quantity: 3  },
    { title: "במכללה", author: "ד''ר לרר", genre: "היסטוריה", available: true, sku: "100029", quantity: 5 },
    { title: "אכן ישנו", author: "עירית יפה", genre: "מדע בדיוני" , available: false, sku: "100030", quantity: 0 },
    { title: "משבצות", author: "חנה גורן", genre: "קומדיה", available: true, sku: "100031", quantity: 2 },
    { title: "מיני בר מיני קר", author: "מאיר בן יאיר", genre: "קומדיה", available: true, sku: "100032", quantity: 7 },
    { title: "לאט אבל בטוח", author: "י.צ.ברלב", genre: "מתח", available: false, sku: "100033", quantity: 0 },
    { title: "כחול הים", author: "עינב רוטשילד", genre: "היסטוריה", available: true, sku: "100034", quantity: 3 },
    { title: "מזמור לתודה", author: "ישראל ברנדסורפר", genre: "קודש", available: true, sku: "100035", quantity: 7 },
    // ... הוסף עוד 345 ספרים כאן
];










// שמירת מערך הספרים ב-localStorage בכל פעם שהדף נטען
localStorage.setItem('books', JSON.stringify(books));

function displayBooks(books) {
    const bookList = document.getElementById('bookList');
    bookList.innerHTML = '';
    books.forEach(book => {
        const li = document.createElement('li');
        li.innerHTML = `
            <strong>${book.title}</strong> מאת ${book.author} (${book.genre})<br>
            מק"ט: ${book.sku} | כמות במלאי: ${book.quantity}
            ${book.available ? 
                `<button onclick="borrowBook('${book.sku}')">השאל ספר</button>` : 
                '<span class="unavailable">לא זמין</span>'}
        `;
        if (!book.available) {
            li.classList.add('unavailable');
        }
        bookList.appendChild(li);
    });
}

// ... שאר הקוד נשאר כפי שהוא










function updateAvailability(books) {
    return books.map(book => ({
        ...book,
        available: book.quantity > 0
    }));
}

function displayBooks(books) {
    const bookList = document.getElementById('bookList');
    bookList.innerHTML = '';
    const updatedBooks = updateAvailability(books);
    updatedBooks.forEach(book => {
        const li = document.createElement('li');
        li.innerHTML = `
            <strong>${book.title}</strong> מאת ${book.author} (${book.genre})<br>
            מק"ט: ${book.sku} | כמות במלאי: ${book.quantity}
        `;
        if (!book.available) {
            li.classList.add('unavailable');
        }
        bookList.appendChild(li);
    });
}

function filterBooks() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const selectedGenre = document.getElementById('genreFilter').value;

    const filteredBooks = books.filter(book => 
        (book.title.toLowerCase().includes(searchTerm) || 
         book.author.toLowerCase().includes(searchTerm) ||
         book.sku.includes(searchTerm)) &&
        (selectedGenre === '' || book.genre === selectedGenre)
    );

    displayBooks(filteredBooks);
}

function searchBySKU() {
    const skuInput = document.getElementById('skuInput').value;
    const foundBook = books.find(book => book.sku === skuInput);
    
    if (foundBook) {
        displayBooks([foundBook]);
    } else {
        alert('לא נמצא ספר עם המק"ט הזה');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    displayBooks(books);

    document.getElementById('searchInput').addEventListener('input', filterBooks);
    document.getElementById('genreFilter').addEventListener('change', filterBooks);
});





localStorage.setItem('books', JSON.stringify(books));










// ... (קוד קיים) ...

function displayBooks(books) {
    const bookList = document.getElementById('bookList');
    bookList.innerHTML = '';
    const updatedBooks = updateAvailability(books);
    updatedBooks.forEach(book => {
        const li = document.createElement('li');
        li.innerHTML = `
            <strong>${book.title}</strong> מאת ${book.author} (${book.genre})<br>
            מק"ט: ${book.sku} | כמות במלאי: ${book.quantity}
            ${book.available ? 
                `<button onclick="borrowBook('${book.sku}')">השאל ספר</button>` : 
                '<span class="unavailable">לא זמין</span>'}
        `;
        if (!book.available) {
            li.classList.add('unavailable');
        }
        bookList.appendChild(li);
    });
}

function borrowBook(sku) {
    // שמירת המק"ט בsessionStorage
    sessionStorage.setItem('borrowingSku', sku);
    // מעבר לדף ההשאלה
    window.location.href = 'borrow_book.html';
}

// ... (שאר הקוד כמו קודם) ...












