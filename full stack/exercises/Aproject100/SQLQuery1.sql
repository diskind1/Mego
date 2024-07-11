-- יצירת טבלת Users
CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50) UNIQUE NOT NULL,
    Password NVARCHAR(100) NOT NULL,
    IsLibrarian BIT NOT NULL DEFAULT 0,
    RegistrationDate DATETIME DEFAULT GETDATE()
);

-- יצירת טבלת Books
CREATE TABLE Books (
    BookID INT PRIMARY KEY IDENTITY(1,1),
    Title NVARCHAR(100) NOT NULL,
    Author NVARCHAR(100) NOT NULL,
    Genre NVARCHAR(50),
    SKU NVARCHAR(20) UNIQUE NOT NULL,
    Quantity INT NOT NULL DEFAULT 0
);

-- יצירת טבלת Loans
CREATE TABLE Loans (
    LoanID INT PRIMARY KEY IDENTITY(1,1),
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    BookID INT FOREIGN KEY REFERENCES Books(BookID),
    LoanDate DATETIME DEFAULT GETDATE(),
    ReturnDate DATETIME
);




-- הוספת משתמשים
INSERT INTO Users (Username, Password, IsLibrarian) VALUES 
('librarian', 'password123', 1),
('user1', 'userpass1', 0),
('user2', 'userpass2', 0);

-- הוספת ספרים
INSERT INTO Books (Title, Author, Genre, SKU, Quantity) VALUES 
('מסע אל תום האלף', 'א.ב. יהושע', 'רומן', 'SKU001', 5),
('1984', 'ג''ורג'' אורוול', 'מדע בדיוני', 'SKU002', 3),
('מלחמה ושלום', 'לב טולסטוי', 'היסטוריה', 'SKU003', 2);



SELECT * FROM Users;
SELECT * FROM Books;
SELECT * FROM Loans;

SELECT @@SERVERNAME


USE LibraryDB;

-- טבלת השאלות
CREATE TABLE Loans (
    LoanID INT PRIMARY KEY IDENTITY(1,1),
    BookSKU NVARCHAR(20) NOT NULL,
    BorrowerName NVARCHAR(100) NOT NULL,
    LoanDate DATE NOT NULL,
    ReturnDate DATE,
    FOREIGN KEY (BookSKU) REFERENCES Books(SKU)
);


USE LibraryDB;
EXEC sp_help 'Loans';

CREATE TABLE BookOrders (
    OrderID INT PRIMARY KEY IDENTITY(1,1),
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    BookID INT FOREIGN KEY REFERENCES Books(BookID),
    OrderDate DATETIME DEFAULT GETDATE()
);