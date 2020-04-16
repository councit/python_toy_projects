


game_markers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def printBoard():
    print(
        '\n',
        game_markers[0],
        game_markers[1],
        game_markers[2], '\n',
        game_markers[3],
        game_markers[4],
        game_markers[5], '\n',
        game_markers[6],
        game_markers[7],
        game_markers[8],
    )


def gameIntro():
    print('Welcome to tic tac toe \n Player one will go first, please select a marker position from 0-8')

def winCheck():
    if(game_markers[0] == character_one_marker and game_markers[1] == character_one_marker and game_markers[2] == character_one_marker):
        print("Player One wins")
        

#Having users pick thier markers. Logic assigned player1 if statements assign user 2 value
while True:
    character_one_marker = input('Player One, please choose your marker. Choose X or O and press enter')
    
    if (character_one_marker == 'X' ):
        player_two_marker = 'O'
    else:
        player_two_marker = 'X'


    if (character_one_marker.upper() == 'X' or character_one_marker.upper() == 'O'):
        print(f'Thank you, Player One is {character_one_marker.upper()}, Player 2 you will be {player_two_marker.upper()} ')

        break
    else:
        print("Please enter X, or O")

    


gameIntro()
printBoard()

while True:
    # Get player one selection
    position_selection = int(input())
    game_markers[position_selection] = character_one_marker
    printBoard()

    # checking for player one win
    if(game_markers[0] == character_one_marker and game_markers[1] == character_one_marker and game_markers[2] == character_one_marker):
        print("Player One wins")
        break
    elif(game_markers[3] == character_one_marker and game_markers[4] == character_one_marker and game_markers[5] == character_one_marker):
        print("Player One wins")
        break
    elif(game_markers[6] == character_one_marker and game_markers[7] == character_one_marker and game_markers[8] == character_one_marker):
        print("Player One wins")
        break
    elif(game_markers[0] == character_one_marker and game_markers[4] == character_one_marker and game_markers[8] == character_one_marker):
        print("Player One wins")
        break
    elif(game_markers[2] == character_one_marker and game_markers[4] == character_one_marker and game_markers[6] == character_one_marker):
        print("Player One wins")
        break


    # get player two selection
    position_selection = int(input())
    game_markers[position_selection] = player_two_marker
    printBoard()

    # checking player two win
    if(game_markers[0] == player_two_marker and game_markers[1] == player_two_marker and game_markers[2] == player_two_marker):
        print("Player One wins")
        break
    elif(game_markers[3] == player_two_marker and game_markers[4] == player_two_marker and game_markers[5] == player_two_marker):
        print("Player One wins")
        break
    elif(game_markers[6] == player_two_marker and game_markers[7] == player_two_marker and game_markers[8] == player_two_marker):
        print("Player One wins")
        break
    elif(game_markers[0] == player_two_marker and game_markers[4] == player_two_marker and game_markers[8] == player_two_marker):
        print("Player One wins")
        break
    elif(game_markers[2] == player_two_marker and game_markers[4] == player_two_marker and game_markers[6] == player_two_marker):
        print("Player One wins")
        break



