import os

default_list = []


def start():
    return [
        ['   ', '|', '   ', '|', '   '],
        ['   ', '|', '   ', '|', '   '],
        ['   ', '|', '   ', '|', '   ']
    ]


def check_for_over(i):
    n = 0

    # Checks for Diagonal Winner
    if default_list[0][0] == default_list[1][2] == default_list[2][4] == f' {i} ' or \
            default_list[0][4] == default_list[1][2] == default_list[2][0] == f' {i} ':
        print(f"{i} won the game!")
        return 0
    else:
        for l in default_list:

            # Checks for Horizontal Winner
            if l == [f' {i} ', '|', f' {i} ', '|', f' {i} ']:
                print(f"{i} won the game!")
                return 0

            # Checks for Vertical Winner
            elif default_list[0][0] == default_list[1][0] == default_list[2][0] == f' {i} ' or \
                    default_list[0][2] == default_list[1][2] == default_list[2][2] == f' {i} ' or \
                    default_list[0][4] == default_list[1][4] == default_list[2][4] == f' {i} ':
                print(f"{i} won the game!")
                return 0

            # Checks if there is Draw
            elif not '   ' in l:
                n += 1
                if n == 3:
                    print('Draw!')
                    return 0
        return 1


def tic_tac_toe(row, col, turn):
    column = 0
    sel_row = default_list[row]
    if col == 1:
        column = 2
    elif col == 2:
        column = 4
    sel_col = sel_row[column]
    if sel_col != '   ':
        print('Oh No! That block is already occupied. Please select another one.')
        user_input = input(f"Please enter {turn}'s input location: ").split(',')
        chance = turn
        try:
            x = int(user_input[0]) - 1
            y = int(user_input[1]) - 1
        except ValueError:
            print("\nPlease type the input numbers in correct way i.e row,column\n")
        except IndexError:
            print("\nPlease type the input numbers in correct way i.e row,column\n")
        except TypeError:
            print("\nPlease type the input numbers in correct way i.e row,column\n")
        else:
            # print(f"x: {x}, y: {y}")
            tic_tac_toe(x, y, chance)
    rep_col = sel_col.replace('   ', f' {turn} ')
    sel_row[column] = rep_col
    default_list[row] = sel_row
    # print(f"sel_col: {rep_col}, default_list: {default_list}")

    output_list = []
    for list in default_list:
        for item in list:
            output_list.append(item)
        output_list.append('\n-----------\n')

    output = "".join(output_list[:-1])
    return "\n" + output + "\n"


def tic_tac_toe_game():
    is_game = True
    global default_list
    default_list = start()
    turn = 0
    while is_game:
        if turn % 2 == 0:
            user_input = input("Please enter X's input location: ").split(',')
            chance = 'X'

        else:
            user_input = input("Please enter O's input location: ").split(',')
            chance = 'O'
        try:
            x = int(user_input[0]) - 1
            y = int(user_input[1]) - 1
            if x <= -1 or x >= 3 or y <= -1 or y >= 3:
                raise ValueError
        except ValueError:
            print("\nPlease type the input numbers (1, 2, 3) in correct way i.e row,column\n")
        except IndexError:
            print("\nPlease type the input numbers (1, 2, 3) in correct way i.e row,column\n")
        else:
            # print(f"x: {x}, y: {y}")
            os.system('cls')
            print(tic_tac_toe(x, y, chance))
            response = check_for_over(chance)
            # print(response)
            if response == 0:
                is_game = False
                user_res = input("\nWant to play again? type 'y' or 'n': ")
                if user_res == 'y':
                    os.system('cls')
                    tic_tac_toe_game()
                elif user_res == 'n':
                    print('\nThanks for playing the game. OwO')
                    print('Please run the program again if you want to play!')
            turn += 1


print(
    """
    The Basic Version of
    ████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗
    ╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝
       ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗  
       ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝  
       ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗
       ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝                                                                                  
                                                                Copyright to: ©Aditya Kore
    """
)
print('Welcome to my Tic-Tac-Toe Game!')
print("It's 2-player game with same rule as of real life game.\n")
print("Make sure to put your input as row,column. For e.g 2,3")
print("Also, remember there are 3 rows and 3 columns.\n")
tic_tac_toe_game()
