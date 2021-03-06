the_board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}


board_keys = []

for key in the_board:
    board_keys.append(key)


def print_board(board):
    print(" ")
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print(" ")
    print("Places number.")
    print('7' + '|' + '8' + '|' + '9')
    print('-+-+-')
    print('4' + '|' + '5' + '|' + '6')
    print('-+-+-')
    print('1' + '|' + '2' + '|' + '3')
    print(" ")

# print_board(the_board)

def game():

    turn = 'X'
    count = 0

    for i in range(10):
        print_board(the_board)
        print("Your turn " + turn + " .Move to which place?")
        try:
            move = input()
            if the_board[move] == ' ':
                the_board[move] = turn
                count += 1
            else:
                print("That place is already filled. \nMove to which place?")
                continue
        except KeyError:
            print('Enter a valid value!')
        # Now we will check if player X or O has won, for every move after 5 move.

        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':
                print_board(the_board)
                print('\n Game Over. \n')
                print(" **** " + turn + " Won." + " **** ")
                break
        elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':
            print_board(the_board)
            print('\n Game Over. \n')
            print(" **** " + turn + " Won." + " **** ")
            break
        elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':
            print_board(the_board)
            print('\n Game Over. \n')
            print(" **** " + turn + " Won." + " **** ")
            break
        elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
            print_board(the_board)
            print('\n Game Over. \n')
            print(" **** " + turn + " Won." + " **** ")
            break
        elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':
            print_board(the_board)
            print('\n Game Over. \n')
            print(" **** " + turn + " Won." + " **** ")
            break
        elif the_board['7'] == the_board['5'] == the_board['3'] != ' ':
            print_board(the_board)
            print('\n Game Over. \n')
            print(" **** " + turn + " Won." + " **** ")
            break
        elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':
            print_board(the_board)
            print('\n Game Over. \n')
            print(" **** " + turn + " Won." + " **** ")
            break
    
        # If neither X nor O wins and the board is full, we'll declare the result as 'Draw'.
        if count == 9:
            print("\nGame over.\n")
            print("It is draw")

        # We have to change the player after every move.
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    # Now we will ask if players wants to restart the game or not.
    restart = input("Do you want to play again!(y/n)")

    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            the_board[key] = ' '
        game()


if __name__ == "__main__":
    game()