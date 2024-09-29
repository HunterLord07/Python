import numpy as np


def print_board():
    for i in range(0, 9, 3):
        j = i + 3
        row = board[i:j]
        print('| ' + ' | '.join(row) + ' |')


def winner(board, player):
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                      [0, 3, 6], [1, 4, 7], [2, 5, 8],
                      [0, 4, 8], [2, 4, 6]]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def draw(board):
    for space in board:
        if space == ' ':
            return False
    if winner(board, 'X') or winner(board, 'O'):
        return False

    return True


def available_moves(board):
    moves = []
    for i in range(9):
        if board[i] == ' ':
            moves.append(i)
    return moves


def evaluate_move(board, comp_turn):
    if winner(board, 'O'):
        return 1  # Computer
    if winner(board, 'X'):
        return -1  # Player
    if draw(board):
        return 0

    best_score = -10
    if not comp_turn:
        best_score = 10

    for move in available_moves(board):
        if comp_turn:
            board[move] = 'O'
        else:
            board[move] = 'X'

        score = evaluate_move(board, not comp_turn)
        board[move] = ' '

        if best_score is None:
            best_score = score
        elif comp_turn:
            best_score = max(score, best_score)
        else:
            best_score = min(score, best_score)

    return best_score


def select_move():
    best_score = -10
    move = -1
    for i in available_moves(board):
        board[i] = 'O'
        score = evaluate_move(board, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i

    return move

board = [' ' for _ in range(9)]
print("Welcome to Tic-Tac-Toe!")
print_board()

game_over = 0
while game_over == 0:
    move = int(input("Enter your move (1-9): "))
    move = move-1
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("Invalid move! Try again.")
        continue
    print_board()

    if winner(board, 'X'):
        print("You win!")
        game_over = 1
        break
    elif draw(board):
        print("It's a draw!")
        game_over = 1
        break

    print("Computer is making a move...")
    possible_moves = available_moves(board)
    move = np.random.choice(possible_moves)
    board[move] = 'O'
    print_board()

    if winner(board, 'O'):
        print("Computer wins!")
        game_over = 1
        break
    elif draw(board):
        print("It's a draw!")
        game_over = 1
        break
