
















# # שאלה 1
# # מספר שלם חיובי נקרא "מספר מושלם" אם הוא מתחלק בסכום ספרותיו.
# # לדוגמה:
# # מספר 12 הוא מספר מושלם, מספר 24 הוא מספר מושלם, מספר 25 אינו מספר מושלם.
# # כתבו קטע תוכנית להדפסת כל המספרים המושלמים מ - 1 עד .1,000 

# def is_perfect_number(num):
#     # חישוב סכום הספרות
#     digit_sum = sum(int(digit) for digit in str(num))
#     # בדיקה אם המספר מתחלק בסכום הספרות
#     return num % digit_sum == 0

# # חיפוש למספרים מושלמים בטווח 1 עד 1,000
# for i in range(1, 1001):
#     if is_perfect_number(i):
#         print(f"{i} is a perfect number")























# # משחק איקס עיגול

# # יצירת לוח משחק
# board = [" " for _ in range(9)]

# def print_board():
#     for i in range(0, 9, 3):
#         print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
#         if i < 6:
#             print("-" * 9)

# def check_winner(player):
#     # בדיקת ניצחון לפי טורים, שורות ואלכסונים
#     winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
#                             (0, 3, 6), (1, 4, 7), (2, 5, 8),
#                             (0, 4, 8), (2, 4, 6)]
#     for combo in winning_combinations:
#         if all(board[i] == player for i in combo):
#             return True
#     return False

# def play_game():
#     current_player = "X"
#     while True:
#         print_board()
#         move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
#         if move < 0 or move >= 9:
#             print("Choose a valid position (1-9).")
#             continue
#         if board[move] == " ":
#             board[move] = current_player
#             if check_winner(current_player):
#                 print_board()
#                 print(f"Player {current_player} wins!")
#                 break
#             current_player = "O" if current_player == "X" else "X"
#         else:
#             print("That position is already taken. Try again.")

# if __name__ == "__main__":
#     play_game()






















# # משחק איקס עיגול

# # יצירת לוח משחק
# board = [" " for _ in range(9)]

# def print_board():
#     for i in range(0, 9, 3):
#         print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
#         if i < 6:
#             print("-" * 9)

# def check_winner(player):
#     # בדיקת ניצחון לפי טורים, שורות ואלכסונים
#     winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
#                             (0, 3, 6), (1, 4, 7), (2, 5, 8),
#                             (0, 4, 8), (2, 4, 6)]
#     for combo in winning_combinations:
#         if all(board[i] == player for i in combo):
#             return True
#     return False

# def play_game():
#     current_player = "X"
#     while True:
#         print_board()
#         move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
#         if board[move] == " ":
#             board[move] = current_player
#             if check_winner(current_player):
#                 print_board()
#                 print(f"Player {current_player} wins!")
#                 break
#             current_player = "O" if current_player == "X" else "X"
#         else:
#             print("That position is already taken. Try again.")

# if __name__ == "__main__":
#     play_game()

