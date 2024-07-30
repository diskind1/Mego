from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# משתנים גלובליים
MOVE_COUNT = 0  # למעקב אחרי חוק 50 המסעים
POSITION_HISTORY = []  # למעקב אחרי חזרה משולשת

class ChessGame:
    def __init__(self):
        self.piece_symbols = {
            'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
            'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',
            ' ': ' '
        }
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.current_player = 'white'
        self.last_move = None
        self.captured_pieces = {'white': [], 'black': []}
        self.king_moved = {'white': False, 'black': False}
        self.rook_moved = {'white': {'king_side': False, 'queen_side': False},
                           'black': {'king_side': False, 'queen_side': False}}
        self.en_passant_target = None

    def is_valid_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col].lower()
        
        print(f"Checking move: {piece} from {start} to {end}")
        
        if self.current_player == 'white' and self.board[start_row][start_col].islower():
            print("Invalid: White's turn but trying to move black piece")
            return False
        if self.current_player == 'black' and self.board[start_row][start_col].isupper():
            print("Invalid: Black's turn but trying to move white piece")
            return False

        if self.board[end_row][end_col] != ' ' and \
           self.board[end_row][end_col].isupper() == self.board[start_row][start_col].isupper():
            print("Invalid: Destination occupied by same color piece")
            return False

        # מניעת אכילת המלך
        if self.board[end_row][end_col].lower() == 'k':
            print("Invalid: Cannot capture the king")
            return False

        if piece == 'p':
            return self.is_valid_pawn_move(start, end)
        elif piece == 'r':
            return self.is_valid_rook_move(start, end)
        elif piece == 'n':
            return self.is_valid_knight_move(start, end)
        elif piece == 'b':
            return self.is_valid_bishop_move(start, end)
        elif piece == 'q':
            return self.is_valid_queen_move(start, end)
        elif piece == 'k':
            if abs(start_col - end_col) == 2:
                return self.is_valid_castling(start, end)
            return self.is_valid_king_move(start, end)
        
        # בדיקה אם המהלך משאיר את המלך בשח
        if self.move_leaves_king_in_check(start, end):
            print("Invalid: Move leaves king in check")
            return False
        
        print("Invalid: Unknown piece")
        return False

    def is_valid_pawn_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        direction = -1 if self.current_player == 'white' else 1

        if start_col == end_col and self.board[end_row][end_col] == ' ':
            if end_row == start_row + direction:
                return True
            if (self.current_player == 'white' and start_row == 6 and end_row == 4) or \
               (self.current_player == 'black' and start_row == 1 and end_row == 3):
                return self.board[start_row + direction][start_col] == ' '
        if abs(start_col - end_col) == 1 and end_row == start_row + direction:
            if self.board[end_row][end_col] != ' ' and \
               self.board[end_row][end_col].isupper() != self.board[start_row][start_col].isupper():
                return True
            # בדיקת הכאה דרך הילוכו
            if self.en_passant_target == (end_row, end_col):
                return True
        return False

    def is_valid_rook_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        
        if start_row == end_row:
            step = 1 if end_col > start_col else -1
            for col in range(start_col + step, end_col, step):
                if self.board[start_row][col] != ' ':
                    return False
            return True
        elif start_col == end_col:
            step = 1 if end_row > start_row else -1
            for row in range(start_row + step, end_row, step):
                if self.board[row][start_col] != ' ':
                    return False
            return True
        return False

    def is_valid_knight_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        return (abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1) or \
               (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2)

    def is_valid_bishop_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        
        if abs(start_row - end_row) == abs(start_col - end_col):
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            row, col = start_row + row_step, start_col + col_step
            while row != end_row and col != end_col:
                if self.board[row][col] != ' ':
                    return False
                row += row_step
                col += col_step
            return True
        return False

    def is_valid_queen_move(self, start, end):
        return self.is_valid_rook_move(start, end) or self.is_valid_bishop_move(start, end)

    def is_valid_king_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        return abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1

    def is_valid_castling(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        
        if self.king_moved[self.current_player]:
            return False
        
        if end_col > start_col:  # קינג סייד
            rook_col = 7
            if self.rook_moved[self.current_player]['king_side']:
                return False
        else:  # קווין סייד
            rook_col = 0
            if self.rook_moved[self.current_player]['queen_side']:
                return False
        
        # בדיקת ריקנות בין המלך לצריח
        direction = 1 if end_col > start_col else -1
        for col in range(start_col + direction, rook_col, direction):
            if self.board[start_row][col] != ' ':
                return False
        
        # בדיקת שח
        if self.is_check():
            return False
        
        # בדיקת מעבר דרך שח
        for col in range(start_col, end_col + direction, direction):
            if self.is_square_under_attack(start_row, col):
                return False
        
        return True

    def is_check(self):
        king_position = None
        for row in range(8):
            for col in range(8):
                if self.board[row][col].lower() == 'k' and \
                   self.board[row][col].isupper() == (self.current_player == 'white'):
                    king_position = (row, col)
                    break
            if king_position:
                break
        
        if not king_position:
            return False

        opponent_color = 'black' if self.current_player == 'white' else 'white'
        for row in range(8):
            for col in range(8):
                if self.board[row][col] != ' ' and \
                   self.board[row][col].isupper() != (self.current_player == 'white'):
                    if self.is_valid_move((row, col), king_position):
                        return True
        return False

    def is_square_under_attack(self, row, col):
        opponent_color = 'black' if self.current_player == 'white' else 'white'
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != ' ' and \
                   self.board[i][j].isupper() == (opponent_color == 'white'):
                    if self.is_valid_move((i, j), (row, col)):
                        return True
        return False

    def move_prevents_check(self, start, end):
        # ביצוע המהלך באופן זמני
        temp_start = self.board[start[0]][start[1]]
        temp_end = self.board[end[0]][end[1]]
        self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = ' '
        
        # בדיקה אם המלך עדיין בשח
        still_in_check = self.is_check()
        
        # החזרת הלוח למצב הקודם
        self.board[start[0]][start[1]] = temp_start
        self.board[end[0]][end[1]] = temp_end
        
        return not still_in_check

    def move_piece(self, start, end):
        global MOVE_COUNT, POSITION_HISTORY
        
        print(f"Attempting move from {start} to {end}")
        if self.is_valid_move(start, end):
            start_row, start_col = start
            end_row, end_col = end
            
            # שמירת המהלך האחרון
            self.last_move = {
                'start': start,
                'end': end,
                'piece_moved': self.board[start_row][start_col],
                'piece_captured': self.board[end_row][end_col]
            }
            
            piece = self.board[start_row][start_col]
            
            # בדיקה אם כלי נאכל
            if self.board[end_row][end_col] != ' ':
                captured_piece = self.board[end_row][end_col]
                self.captured_pieces['white' if self.current_player == 'black' else 'black'].append(captured_piece)
            
            # טיפול בהכאה דרך הילוכו
            if piece.lower() == 'p' and (end_row, end_col) == self.en_passant_target:
                self.board[start_row][end_col] = ' '  # הסרת הרגלי שהוכה
            
            # ביצוע המהלך
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = ' '
            
            # עדכון הכאה דרך הילוכו
            self.en_passant_target = None
            if piece.lower() == 'p' and abs(start_row - end_row) == 2:
                self.en_passant_target = ((start_row + end_row) // 2, start_col)
            
            # טיפול בהעלאת רגלי
            available_pieces = None
            if piece.lower() == 'p' and (end_row == 0 or end_row == 7):
                available_pieces = [p for p in self.captured_pieces[self.current_player] if p.lower() != 'p']
                if not available_pieces:
                    self.board[end_row][end_col] = 'Q' if piece.isupper() else 'q'  # ברירת מחדל למלכה
            
            # עדכון מצב הצרחה
            if piece.lower() == 'k':
                self.king_moved[self.current_player] = True
                if abs(start_col - end_col) == 2:  # הצרחה
                    rook_start_col = 7 if end_col > start_col else 0
                    rook_end_col = (start_col + end_col) // 2
                    self.board[start_row][rook_end_col] = self.board[start_row][rook_start_col]
                    self.board[start_row][rook_start_col] = ' '
            elif piece.lower() == 'r':
                if start_col == 0:
                    self.rook_moved[self.current_player]['queen_side'] = True
                elif start_col == 7:
                    self.rook_moved[self.current_player]['king_side'] = True
            
            # עדכון מונה המהלכים לחוק 50 המסעים
            if piece.lower() == 'p' or self.board[end_row][end_col] != ' ':
                MOVE_COUNT = 0
            else:
                MOVE_COUNT += 1
            
            # עדכון היסטוריית העמדות
            POSITION_HISTORY.append(self.get_position_key())
            
            # החלפת תור
            self.current_player = 'black' if self.current_player == 'white' else 'white'
            
            is_in_check = self.is_check()
            if is_in_check:
                print(f"Check! {self.current_player}'s king is under attack.")
            
            # בדיקת סיום משחק
            if self.is_checkmate():
                print(f"Checkmate! {self.current_player} loses.")
            elif self.is_stalemate():
                print("Stalemate! The game is a draw.")
            elif self.is_insufficient_material():
                print("Insufficient material! The game is a draw.")
            elif self.is_threefold_repetition():
                print("Threefold repetition! The game is a draw.")
            elif MOVE_COUNT >= 100:
                print("50-move rule! The game is a draw.")
            
            print(f"Move successful. New current player: {self.current_player}")
            return True, is_in_check, available_pieces
        print("Move is invalid")
        return False, False, None

    def promote_pawn(self, end, chosen_piece):
        end_row, end_col = end
        if chosen_piece in self.captured_pieces[self.current_player]:
            self.board[end_row][end_col] = chosen_piece
            self.captured_pieces[self.current_player].remove(chosen_piece)
            return True
        return False

    def get_position_key(self):
        # יצירת מפתח ייחודי למצב הלוח הנוכחי
        return ''.join([''.join(row) for row in self.board]) + self.current_player

    def is_checkmate(self):
        if not self.is_check():
            return False
        return self.no_legal_moves()

    def is_stalemate(self):
        if self.is_check():
            return False
        return self.no_legal_moves()

    def no_legal_moves(self):
        for row in range(8):
            for col in range(8):
                if self.board[row][col] != ' ' and self.board[row][col].isupper() == (self.current_player == 'white'):
                    for end_row in range(8):
                        for end_col in range(8):
                            if self.is_valid_move((row, col), (end_row, end_col)):
                                return False
        return True

    def is_insufficient_material(self):
        pieces = {'K': 0, 'k': 0, 'Q': 0, 'q': 0, 'R': 0, 'r': 0, 'B': 0, 'b': 0, 'N': 0, 'n': 0, 'P': 0, 'p': 0}
        for row in self.board:
            for piece in row:
                if piece in pieces:
                    pieces[piece] += 1
        
        # מלך מול מלך
        if sum(pieces.values()) == 2:
            return True
        # מלך ופרש/רץ מול מלך
        if sum(pieces.values()) == 3 and (pieces['N'] + pieces['n'] == 1 or pieces['B'] + pieces['b'] == 1):
            return True
        return False

    def is_threefold_repetition(self):
        current_position = self.get_position_key()
        return POSITION_HISTORY.count(current_position) >= 3

    def move_leaves_king_in_check(self, start, end):
        # ביצוע המהלך באופן זמני
        temp_start = self.board[start[0]][start[1]]
        temp_end = self.board[end[0]][end[1]]
        self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = ' '
        
        # בדיקה אם המלך בשח
        in_check = self.is_check()
        
        # החזרת הלוח למצב הקודם
        self.board[start[0]][start[1]] = temp_start
        self.board[end[0]][end[1]] = temp_end
        
        return in_check

    def undo_last_move(self):
        if self.last_move:
            start = self.last_move['start']
            end = self.last_move['end']
            self.board[start[0]][start[1]] = self.last_move['piece_moved']
            self.board[end[0]][end[1]] = self.last_move['piece_captured']
            self.current_player = 'white' if self.current_player == 'black' else 'black'
            
            # החזרת כלי שנאכל (אם היה כזה)
            if self.last_move['piece_captured'] != ' ':
                self.captured_pieces[self.current_player].append(self.last_move['piece_captured'])

            # טיפול בביטול העלאת רגלי
            if self.last_move['piece_moved'].lower() == 'p' and (end[0] == 0 or end[0] == 7):
                promoted_piece = self.board[end[0]][end[1]]
                if promoted_piece != self.last_move['piece_moved']:
                    self.captured_pieces[self.current_player].append(promoted_piece)

            # ביטול עדכון מצב הצרחה
            if self.last_move['piece_moved'].lower() == 'k':
                self.king_moved[self.current_player] = False
            elif self.last_move['piece_moved'].lower() == 'r':
                if self.last_move['start'][1] == 0:
                    self.rook_moved[self.current_player]['queen_side'] = False
                elif self.last_move['start'][1] == 7:
                    self.rook_moved[self.current_player]['king_side'] = False
            
            self.last_move = None
            return True
        return False

game = ChessGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_board')
def get_board():
    return jsonify({
        'board': [[game.piece_symbols[piece] for piece in row] for row in game.board],
        'currentPlayer': game.current_player,
        'capturedPieces': {color: [game.piece_symbols[piece] for piece in pieces] 
                           for color, pieces in game.captured_pieces.items()}
    })

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    print("Received move data:", data)
    if not data or 'start' not in data or 'end' not in data:
        return jsonify({'error': 'Invalid data format'}), 400
    start = data['start']
    end = data['end']
    if not all(isinstance(coord, int) for coord in start + end):
        return jsonify({'error': 'Coordinates must be integers'}), 400
    move_success, is_check, available_pieces = game.move_piece(start, end)
    if move_success:
        response_data = {
            'board': [[game.piece_symbols[piece] for piece in row] for row in game.board],
            'currentPlayer': game.current_player,
            'capturedPieces': {color: [game.piece_symbols[piece] for piece in pieces] 
                               for color, pieces in game.captured_pieces.items()},
            'isCheck': is_check
        }
        if available_pieces:
            response_data['availablePieces'] = [game.piece_symbols[piece] for piece in available_pieces]
        return jsonify(response_data)
    else:
        return jsonify({'error': 'Invalid move'}), 400

@app.route('/promote', methods=['POST'])
def promote():
    data = request.json
    if not data or 'end' not in data or 'chosenPiece' not in data:
        return jsonify({'error': 'Invalid data format'}), 400
    end = data['end']
    chosen_piece = data['chosenPiece']
    if game.promote_pawn(end, chosen_piece):
        return jsonify({
            'board': [[game.piece_symbols[piece] for piece in row] for row in game.board],
            'currentPlayer': game.current_player,
            'capturedPieces': {color: [game.piece_symbols[piece] for piece in pieces] 
                               for color, pieces in game.captured_pieces.items()}
        })
    else:
        return jsonify({'error': 'Invalid promotion'}), 400

@app.route('/undo', methods=['POST'])
def undo():
    if game.undo_last_move():
        return jsonify({
            'board': [[game.piece_symbols[piece] for piece in row] for row in game.board],
            'currentPlayer': game.current_player,
            'capturedPieces': {color: [game.piece_symbols[piece] for piece in pieces] 
                               for color, pieces in game.captured_pieces.items()}
        })
    else:
        return jsonify({'error': 'No move to undo'}), 400

if __name__ == '__main__':
    app.run(debug=True)