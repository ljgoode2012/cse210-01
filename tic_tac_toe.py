#Week 2 Prove: Developer - Tic-Tac-Toe
#Author: Lindsey Goode

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_open = True
change = False
turn = 'x'

def main():
    print('Welcome to Tic-Tac-Toe!\n')
    while game_open == True:
        print
        print_table()
        print()
        if turn == 'x':
            players_choice = int(input("x's turn to choose a square (1-9):"))
        elif turn == 'o':
            players_choice = int(input("o's turn to choose a square (1-9):"))
        run_turn(players_choice, turn)
        if change == True:
            change_turn()
        #check_game_status()
    
def print_table():
    seperator = '-+-+-'
    line_1 = f'{list[0]}|{list[1]}|{list[2]}'
    line_2 = f'{list[3]}|{list[4]}|{list[5]}'
    line_3 = f'{list[6]}|{list[7]}|{list[8]}'
    print(f'{line_1}\n{seperator}\n{line_2}\n{seperator}\n{line_3}')

def run_turn(players_choice, turn):
    global change
    if players_choice in list:
        choice_index = list.index(players_choice)
        list[choice_index] = turn
        change = True
    else:
        print("Entry not valid. Please enter an integer between 1 and 9.")
        change = False

def change_turn():
    global turn
    if turn == 'x':
        turn = 'o'
    elif turn == 'o':
        turn = 'x'
    









if __name__ == '__main__':
    main()