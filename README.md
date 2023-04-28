# pawn-stars

## Collaborators:
Barsoum Basta, Colby Brudin, Daniel Dean, Jamin Valick, Jiwoong Jeon, Nicholas Glaz

## Libraries:
https://pypi.org/project/chess/
\
https://pypi.org/project/tensorflow/
\
https://pypi.org/project/stockfish/
\
https://pypi.org/project/pgn-parser/

Libraries such as pandas and numpy were also used, and all can be found at the top of modelcode.ipynb

## Overview:

The modelcode.ipynb file contains all of the necessary code to get the dataset, create and train the model, and utilize the model's predictions. 

The dataset is created by parsing through a large file from Lichess.org, which contains thousands of games played by 2000+ rated master-level players. This file is included in a zip, and must be extracted (and potentailly renamed) to be used in this program. The first 1000 games are extracted, and every position where it is white's move is added to the master training set, as well as the expected move output, which is just the move that white made in the game. A test set of 100 games was also created to verify the model's accuracy later. The moves are obtained in FEN notation (https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) and are then converted to the proper format using some of the functions desribed below.

After obtaining the dataset, a model is created. It used 2 sets Conv2D layers paired with MaxPooling layers, followed by a Flatten layer and 2 Dense layers that eventually produce the output. The output is formatted as 4 decimals between 0 and 1, which correspond to the starting row and column and ending row and column of the move to be played. For example, if the target move is e2e4, the expected output would be [0.625, 0.25, 0.625, 0.5], which when taken as a fraction out of 8 becomes [5,2,5,4] which is the same as [e,2,e,4].

The model is then optimized and trained, although the model quickly begins to reach the point where validation loss starts increasing. Due to this, the number of epochs should be kept low, at least until a better model is devised. 

To test the model, three methods are provided: random positions, full game against random move opponent, and full game against human opponent. For the random position option, a random position is taken from the test set and evaluated by Stockfish 15. Then, our model and a random move generator both make a move and the next boards are evaluated by Stockfish. Whichever move provided the best change in evaluation (almost always least loss of centipawns rather than gain) would be declared the winner of that round. For the next two options of playing against a random move generator or human opponent, the model just plays the white moves, and if an illegal move is suggested a random one is played instead.

The model ended up being awful at playing chess, but was fairly better than randomness at predicting moves in random positions. 

## Helper Functions:

### board_fen_to_8x8:
Input: FEN notation for a chess board
Output: an 8-by-8 grid corresponding to the rows and columns of the chessboard, where 0's are put in place of blanks

### letter_to_number:
Input: a letter corresponding to a piece
Output: a number between -6 and 6 (not 0) that catagorizes the piece in the form of an integer

### board_to_nums:
Input: a chess board (in array notation from board_fen_to_8x8 method)
Output: the same board but with the letters mapped to numbers between -6 and 6.

### board_to_12_array:
Input: a chess board (in array notation from board_fen_to_8x8 method)
Output: a 3D-array consisting of 12 8-by-8 arrays that each correspond to the specific locations of a piece on the chessboard. For example, one of the arrays would be the position of all 8 (or less) white pawns on the board, with a 1 in the location they are in and 0's everywhere else.
