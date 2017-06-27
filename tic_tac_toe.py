
import os

def draw_board(board):
    print()
    print('     TIC TAC TOE')
    print()
    print()
    print('       |     |')
    print('    ' + board[7] + '  | ' + board[8] + '   | ' + board[9])
    print('       |     |')
    print('  -----------------')
    print('       |     |')
    print('    ' + board[4] + '  | ' + board[5] + '   | ' + board[6])
    print('       |     |')
    print('  -----------------')
    print('       |     |')
    print('    ' + board[1] + '  | ' + board[2] + '   | ' + board[3])
    print('       |     |')
    
def check_draw():
    #board list full

    if board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ' :
        print('TIE.')
        exit()

def check_win():
    win = ['x', 'x', 'x']
    win2 = ['o', 'o', 'o']
    player1_win = 0
    player2_win = 0

    #player1 wins:
    #123
    if win[0] == board[1] and win[1] == board[2] and win[2] == board[3]:
        player1_win = 1
        if player1_win == 1:
            print('Player_1 wins')
            game_is_on = False
            exit()

    #456
    elif win[0] == board[4] and win[1] == board[5] and win[2] == board[6]:
        player1_win = 1
        if player1_win == 1:
            print('Player_1 wins')
            game_is_on = False
            exit()
    #789
    elif win[0] == board[7] and win[1] == board[8] and win[2] == board[9]:
        player1_win = 1
        if player1_win == 1:
            print('Player_1 wins')
            game_is_on = False
            exit()
    #147
    elif win[0] == board[1] and win[1] == board[4] and win[2] == board[7]:
        player1_win = 1
        if player1_win == 1:
            print('Player_1 wins')
            game_is_on = False
            exit()
    #258
    elif win[0] == board[2] and win[1] == board[5] and win[2] == board[8]:
        player1_win = 1
        if player1_win == 1:
            print('Player_1 wins')
            game_is_on = False
            exit()
    #369
    elif win[0] == board[3] and win[1] == board[6] and win[2] == board[9]:
        player1_win = 1
        if player1_win == 1:
            print('Player_1 wins')
            game_is_on = False
            exit()
    #159
    elif win[0] == board[1] and win[1] == board[5] and win[2] == board[9]:
        player1_win = 1
        if player1_win == 1:
            print('Player_1 wins')
            game_is_on = False
            exit()
    #357
    elif win[0] == board[3] and win[1] == board[5] and win[2] == board[7]:
        player1_win = 1
        if player1_win == 1:
            print('Player_1 wins')
            game_is_on = False
            exit()

    #player2 wins:
    elif win2[0] == board[1] and win2[1] == board[2] and win2[2] == board[3]:
        player2_win = 1
        if player2_win == 1:
            print('Player_2 wins')
            game_is_on = False
            exit()
    #456
    elif win2[0] == board[4] and win2[1] == board[5] and win2[2] == board[6]:
        player2_win = 1
        if player2_win == 1:
            print('Player_2 wins')
            game_is_on = False
            exit()
    #789
    elif win2[0] == board[7] and win2[1] == board[8] and win2[2] == board[9]:
        player2_win = 1
        if player2_win == 1:
            print('Player_2 wins')
            game_is_on = False
            exit()
    #147
    elif win2[0] == board[1] and win2[1] == board[4] and win2[2] == board[7]:
        player2_win = 1
        if player2_win == 1:
            print('Player_2 wins')
            game_is_on = False
            exit()
    #258
    elif win2[0] == board[2] and win2[1] == board[5] and win2[2] == board[8]:
        player2_win = 1
        if player2_win == 1:
            print('Player_2 wins')
            game_is_on = False
            exit()
    #369
    elif win2[0] == board[3] and win2[1] == board[6] and win2[2] == board[9]:
        player2_win = 1
        if player2_win == 1:
            print('Player_2 wins')
            game_is_on = False
            exit()
    #159
    elif win2[0] == board[1] and win2[1] == board[5] and win2[2] == board[9]:
        player2_win = 1
        if player2_win == 1:
            print('Player_2 wins')
            game_is_on = False
            exit()
    #357
    elif win2[0] == board[3] and win2[1] == board[5] and win2[2] == board[7]:
        player2_win = 1
        if player2_win == 1:
            print('Player_2 wins')
            game_is_on = False
            exit()
    else:
        pass


def upd_list():
    try:
        while True:
            a = input()
            a = int(a)
            b = board[a]    
            if turn == player1:
                if b == ' ':
                    board[a] = 'x'
                    break
                else:
                    print('square already used')
            else:
                if turn == player2:
                    if b == ' ':
                        board[a] = 'o'
                        break
                    else:
                        print('square already used')
    except ValueError:
        print("Not a number")
        


while True:
    os.system('clear') 
    board = [' '] * 10
    player1 = 1
    player2 = 2
    turn = player1
    draw_board(board)
    print('Player_1 starts the game' '\n')
    game_is_on = True

    while game_is_on:
        if turn == player1:
            print('\n' 'Player_1  Make your move')
            upd_list()
            os.system('clear')
            draw_board(board)
            check_win()
            check_draw()
            turn = player2
        else:
            turn == player2
            print('\n' 'Player_2  Make your move')
            upd_list()
            os.system('clear')
            draw_board(board)
            check_win()
            check_draw()
            turn = player1

