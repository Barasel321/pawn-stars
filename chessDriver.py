import chess
import random


def make_move(move):

    if(move in board.legal_moves):
        board.push(move)
    else:
        return("not legal")
    
    if(board.is_game_over()):
        return(board.outcome())
    else:
        return(move)


board = chess.Board()

while not board.is_game_over():
    move = random.choice([move for move in board.legal_moves])
    gameStatus = make_move(move)
    print(gameStatus)
    print(board)