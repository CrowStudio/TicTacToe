'''
Tic Tac Toe
'''

import os
import string
from colorama import Fore

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

start_game = 1
keep_playing = 1
new_game = 1

tic = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Function: Setup of game elements
# - Arguments: N/A
# - Returns: (frame setup)
def set_board():
    '''
    Set game board
    '''

    if start_game == 0:
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n\n')

    # Setup frame elements.
    print('****' + '***'+ '***' +'*****'+ '***' + '***' + '****\n'+

          '*       '    +  '*       '    +  '*   '+      '    *\n'+

          '*   '+tic[7]+'   *   '+tic[8]+'   *   '+tic[9]+'   *\n'+

          '*       '    +  '*       '    +  '*   '+      '    *\n'+

          '****' + '***'+ '***' +'*****'+ '***' + '***' + '****\n'+

          '*       '    +  '*       '    +  '*   '+      '    *\n'+

          '*   '+tic[4]+'   *   '+tic[5]+'   *   '+tic[6]+'   *\n'+

          '*       '    +  '*       '    +  '*   '+      '    *\n'+

          '****' + '***'+ '***' +'*****'+ '***' + '***' + '****\n'+

          '*       '    +  '*       '    +  '*   '+      '    *\n'+

          '*   '+tic[1]+'   *   '+tic[2]+'   *   '+tic[3]+'   *\n'+

          '*       '    +  '*       '    +  '*   '+      '    *\n'+

          '****' + '***'+ '***' +'*****'+ '***' + '***' + '****')


# Function: Do you want to play?
# - Arguments: N/A
# - Returns (keep playing, start new or end game)
def wanna_play():
    '''
    Wanna play?
    '''

    answer = ''

    # Loop as long as input is incorrect
    while answer == '':

        answer = input('Yes (y) or No (n): ')
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # If a equals Y
        # - Start new game
        if answer.upper() == 'Y':
            keep_playing = 1
            new_game = 1
        # Else if a equals N
        # - End game
        elif answer.upper() == 'N':
            keep_playing = 0
            new_game = 0
            print('See you another time!\n\n')
        # Else
        # - Icorrect input! Ask again
        else:
            answer = ''
            # Clear screen
            #os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.LIGHTRED_EX + 'Incorrect input! Only Y (y) or N (n) is allowed!\n'
                  + Fore.RESET)
            print('Try again!')

    return keep_playing, new_game


# Function: Assign X an O to players
# - Arguments: N/A
# - Returns: (marker for player 1, marker for player 2)
def set_player():
    '''
    Set player
    '''

    p1 = ''

    # While player not set
    while p1 == '':

        p = input('Player 1: Do you want to play X or O? ')

        if p.upper() == 'X':
            p1 = 'X'
            print('Player 2: You are O\n')
        elif p.upper() == 'O':
            p1 = 'O'
            print('Player 2: You are X\n')
        else:
            # Clear screen
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.LIGHTRED_EX + 'Invalid input! Only X (x) or O (o) is allowed!\n'
                  + Fore.RESET)
            print('Try again!')

    return p1


# Function: SET or MOVE marker depending on turn and player
# - Arguments: (n of turns for player 1, n of turns for player 2, player)
# - Returns:
#   (marker to SET, marker to MOVE, marker, n of turns for player 1, n of turns for player 2)
def make_move(turns1, turns2, player):
    '''
    Make a move
    '''

    rm = ''
    num = ''

    # Determine player marker
    if player == 1 and player1 == 'O':
        markerXO = 'O'
    else:
        if player == 2 and player2 == 'O':
            markerXO = 'O'
        else:
            markerXO = 'X'


    # Function: Check input for incorrect charaters
    # - Arguments (charater to check)
    # - Returns: (character)
    def check_input(x):
        '''
        Check input
        '''

        # Assign string of alphabet with lower case
        alphabet = string.ascii_lowercase

        # Checks that input is 1-9
        for c in alphabet:
            #If x is character in aplphabet or empty string or if lenght of string is greater than 1
            if x.lower() == c or x.lower() == '' or len(x) > 1:
                x = 0
                break

        # If x eqauls 0
        # - Incorrect input!
        if x == 0:
            print(Fore.LIGHTRED_EX + '\nIncorrect input, must be 1-9, try again!' + Fore.RESET)

            return ''

        # Return correct input
        return x


    # Function: Check if leagal move for marker to MOVE
    # - Arguments: N/A
    # - Returns: (rm)
    def move_marker():
        '''
        Move marker
        '''

        # If placed marker does NOT equals removed marker
        # - Illegal move!
        if not tic[rm] == markerXO:
            print(Fore.LIGHTRED_EX + f'\nIleagal move, you can only MOVE {markerXO}!' + Fore.RESET)
            return ''

        # Retrun correct marker to MOVE
        return rm

    # Function: Check if leagal move for marker to SET
    # - Arguments: N/A
    # - Returns: (num)
    def set_marker():
        '''
        Set marker
        '''

        # If box for marker NOT equals empty
        # - Illegal move!
        if num == 0 or not tic[num] == ' ':
            print(Fore.LIGHTRED_EX + f'\nIleagal move, you can only SET {markerXO}'
                  + ' in empty space!' + Fore.RESET)
            return ''

        # Retrun correct marker to SET
        return num


    # If player played threee or more turns
    # - Ask which marker to move and then ask where to place marker
    if player == 1 and turns1 >= 3 or player == 2 and turns2 >= 3:

        # Loop as long as input is incorrect
        while rm == '':
            rm = input(f'\nPlayer {player}, enter marker to MOVE: ')
            rm = check_input(rm)

            # If rm NOT equals string
            # - Cast string to int and check if legal move
            if rm != '':
                rm = int(rm)
                rm = move_marker()


       # Loop as long as input is incorrect
        while num == '':
            num = input(f'\nPlace your marker Player {player}: ')
            num = check_input(num)

            # If num NOT equals string
            # - Cast string to int and check if legal move
            if num != '':
                num = int(num)
                num = set_marker()

     # Else if player played less than 3 turns
    # - Ask where to place marker
    elif  player == 1 and turns1 < 3 or player == 2 and turns2 < 3:

        # Loop as long as input is incorrect
        while num == '':
            num = input(f'\nPlace your marker Player {player}: ')
            num = check_input(num)

            # If num NOT equals string
            # - Cast string to int and check if legal move
            if num != '':
                num = int(num)
                num = set_marker()

        # No marker to MOVE
        rm = 0

    # Add 1 to players turn
    if player == 1:
        turns1 += 1
    elif player == 2:
        turns2 += 1

    return num, rm, markerXO, turns1, turns2


# Function: Evaluate game
# - Arguments: N/A
# - Returns: (keep playing, start new or end game)
def evaluate():
    '''
    Look for a winner!
    '''

    # If three X in a row
    # - Set winner to X
    if (tic[7] == tic[8] == tic[9] == 'X' or
            tic[4] == tic[5] == tic[6] == 'X' or
            tic[1] == tic[2] == tic[3] == 'X' or
            tic[7] == tic[5] == tic[3] == 'X' or
            tic[1] == tic[5] == tic[9] == 'X' or
            tic[1] == tic[2] == tic[3] == 'X' or
            tic[7] == tic[4] == tic[1] == 'X' or
            tic[8] == tic[5] == tic[2] == 'X' or
            tic[9] == tic[6] == tic[3] == 'X'):
        winner = 'X'
    # Else if O three in a row
    # - Set winner to O
    elif (tic[7] == tic[8] == tic[9] == 'O' or
          tic[4] == tic[5] == tic[6] == 'O' or
          tic[1] == tic[2] == tic[3] == 'O' or
          tic[7] == tic[5] == tic[3] == 'O' or
          tic[1] == tic[5] == tic[9] == 'O' or
          tic[1] == tic[2] == tic[3] == 'O' or
          tic[7] == tic[4] == tic[1] == 'O' or
          tic[8] == tic[5] == tic[2] == 'O' or
          tic[9] == tic[6] == tic[3] == 'O'):
        winner = 'O'
    else:
        winner = 0

    # If winner is X or O
    # - Print winner and ask for new game
    if winner in ('X', 'O'):
        for x in range(len(tic)):
            if tic[x] == winner:
                tic[x] = Fore.GREEN + winner + Fore.RESET

        set_board()

        print('Congratulations' + Fore.GREEN + f' Player {winner}'
              + Fore.RESET + ', you won!')

        print('\nDo you want to play again,')
        keep_playing, new_game = wanna_play()

        return keep_playing, new_game
    elif turns1 == 18 and turns2 == 18:

        print(Fore.CYAN + 'You are too smart for eachother, it\'s a draw!'+ Fore.RESET)

        print('\nDo you want to play again,')
        keep_playing, new_game = wanna_play()

        return keep_playing, new_game

    # Else
    # - Keep playing
    else:
        keep_playing = 1
        new_game = 0

        return keep_playing, new_game


# Tic Tac Toe - The Game
while keep_playing == 1:


    # If new_game
    # - Reset and print game board
    if new_game == 1:

        player = 1

        player1 = 'O'
        turns1 = 0

        player2 = 'O'
        turns2 = 0

        # If start_game equals 1
        # - Show welcome message and numbers for placement
        if start_game == 1:
            print('\nWelcome to Tic Tac Toe!')
            print('Use NumPad or 1-9 to place marker according to game board below:\n')
            tic = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']

            # Print game board with numbers according to NumPad
            set_board()

            print('\nAre you ready to play?')
            keep_playing, new_game = wanna_play()

            # If you do not wanna play
            # - Exit loop
            if keep_playing == 0:
                break

        # - Reset board
        tic = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        sp = set_player()
        # Depending on what player 1 has choosen
        if sp == 'X':
            X = 1
            player1 = 'X'
        elif sp == 'O':
            O = 1
            player2 = 'X'

        # Print game board
        set_board()

        # Game started
        start_game = 0
        new_game = 0

    # Else
    # - Play game and set marker depending on player and keypress
    else:

        # Make move
        num, rm, markerXO, turns1, turns2 = make_move(turns1, turns2, player)

        # MOVE marker
        tic[rm] = ' '
        # SET marker
        tic[num] = markerXO

        # Switch player
        if player == 1:
            player = 2
        else:
            player = 1

        # Set new frame with markers
        set_board()

        # Look for a winner
        keep_playing, new_game = evaluate()
