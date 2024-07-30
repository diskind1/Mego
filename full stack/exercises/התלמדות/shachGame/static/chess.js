const chessboard = document.getElementById('chessboard');
const currentPlayerDisplay = document.getElementById('current-player');
const undoButton = document.getElementById('undo-button');
const whiteCapturedDisplay = document.getElementById('white-captured');
const blackCapturedDisplay = document.getElementById('black-captured');
const alertsDisplay = document.getElementById('alerts');

let board = [];
let currentPlayer = 'white';
let selectedPiece = null;

function createBoard() {
    chessboard.innerHTML = '';
    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            const square = document.createElement('div');
            square.className = `square ${(row + col) % 2 === 0 ? 'white' : 'black'}`;
            square.dataset.row = row;
            square.dataset.col = col;
            square.addEventListener('click', handleSquareClick);
            chessboard.appendChild(square);
        }
    }
    updateBoard();
}

function updateBoard() {
    fetch('/get_board')
        .then(response => response.json())
        .then(data => {
            board = data.board;
            currentPlayer = data.currentPlayer;
            for (let row = 0; row < 8; row++) {
                for (let col = 0; col < 8; col++) {
                    const square = chessboard.children[row * 8 + col];
                    square.textContent = board[row][col];
                    square.className = `square ${(row + col) % 2 === 0 ? 'white' : 'black'}`;
                    if ('♔♕♖♗♘♙'.includes(board[row][col])) {
                        square.classList.add('white-piece');
                    } else if ('♚♛♜♝♞♟'.includes(board[row][col])) {
                        square.classList.add('black-piece');
                    }
                }
            }
            currentPlayerDisplay.textContent = currentPlayer === 'white' ? 'לבן' : 'שחור';
            updateCapturedPieces(data.capturedPieces);
        });
}

function updateCapturedPieces(capturedPieces) {
    whiteCapturedDisplay.textContent = capturedPieces.white.join(' ');
    blackCapturedDisplay.textContent = capturedPieces.black.join(' ');
}

function handleSquareClick(event) {
    const square = event.target;
    const row = parseInt(square.dataset.row);
    const col = parseInt(square.dataset.col);

    if (selectedPiece === null) {
        if (board[row][col] !== ' ' && isPieceOfCurrentPlayer(board[row][col])) {
            selectedPiece = { row, col };
            square.classList.add('selected');
        }
    } else {
        movePiece(selectedPiece.row, selectedPiece.col, row, col);
        chessboard.children[selectedPiece.row * 8 + selectedPiece.col].classList.remove('selected');
        selectedPiece = null;
    }
}

function isPieceOfCurrentPlayer(piece) {
    return (currentPlayer === 'white' && '♔♕♖♗♘♙'.includes(piece)) || 
           (currentPlayer === 'black' && '♚♛♜♝♞♟'.includes(piece));
}






function movePiece(fromRow, fromCol, toRow, toCol) {
    console.log(`Attempting to move from (${fromRow}, ${fromCol}) to (${toRow}, ${toCol})`);
    fetch('/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            start: [fromRow, fromCol],
            end: [toRow, toCol]
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error('Error:', data.error);
            alert(data.error);
        } else {
            console.log('Move successful');
            updateBoard();
            if (data.isCheck) {
                alertsDisplay.textContent = `שח! המלך של ${data.currentPlayer === 'white' ? 'שחור' : 'לבן'} תחת איום.`;
            } else {
                alertsDisplay.textContent = '';
            }
            if (data.availablePieces) {
                promptPawnPromotion(toRow, toCol, data.availablePieces);
            }
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function promptPawnPromotion(row, col, availablePieces) {
    const promotionDialog = document.createElement('div');
    promotionDialog.id = 'promotion-dialog';
    promotionDialog.innerHTML = `
        <h3>בחר כלי להחלפת החייל:</h3>
        ${availablePieces.map(piece => `<button class="promotion-piece">${piece}</button>`).join('')}
    `;
    document.body.appendChild(promotionDialog);

    promotionDialog.querySelectorAll('.promotion-piece').forEach(button => {
        button.addEventListener('click', () => {
            const chosenPiece = button.textContent;
            promotePawn(row, col, chosenPiece);
            document.body.removeChild(promotionDialog);
        });
    });
}

function promotePawn(row, col, chosenPiece) {
    fetch('/promote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            end: [row, col],
            chosenPiece: chosenPiece
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error('Error:', data.error);
            alert(data.error);
        } else {
            console.log('Promotion successful');
            updateBoard();
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}




function undoLastMove() {
    fetch('/undo', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error('Error:', data.error);
            alert(data.error);
        } else {
            console.log('Undo successful');
            updateBoard();
            alertsDisplay.textContent = '';
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

undoButton.addEventListener('click', undoLastMove);

createBoard();