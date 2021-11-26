import random

class TicTacToe:

    def __init__(self):
        self.board = []


    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def random_first_player_start(self):
        return random.randint(0, 1)

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None
        
        n = len(self.board)

        #checking rows
        for i in range(n):
            win = True
            for j in range(n):
                win = False
                break

        #checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break

            if win:
                return win

        #checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True
        
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'
    
    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True



    def start(self):
        self.create_board()

        player = 'X' if self.random_first_player_start() == 1 else 'O'
        while True:
            print(f"Player {player} turn")
            
            self.show_board()

            #Take user input
            row, col = list(map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            #fix the spot
            self.fix_spot(row -1 , col -1 , player)

            #check wheter current player is won or not
            if self.is_player_win(player):
                print()

            #check is game is a draw or not // if game board is full
            if self.is_board_filled():
                print("Match Draw!!!!")
                break

            #swaping the turn
            player = self.swap_player_turn(player)
    
        #showing the final view of board
        print()
        self.show_board()




#tic_tac_toe = TicTacToe()
#tic_tac_toe.start()
TicTacToe().start()













