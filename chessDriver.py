import chess
import random


#make move on chess object based on given move
def make_move(move):

    #make move if move is lega, else return "not legal"
    if(move in board.legal_moves):
        board.push(move)
    else:
        return("not legal")
    
    #check if game has ended and return outcome else return move made
    if(board.is_game_over()):
        return(board.outcome())
    else:
        return(move)


#chess object
board = chess.Board()

#play game with random moves
while not board.is_game_over():
    move = random.choice([move for move in board.legal_moves])
    gameStatus = make_move(move)
    print(gameStatus)
    print(board)