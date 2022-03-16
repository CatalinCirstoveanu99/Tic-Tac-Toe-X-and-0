import random, re, os
from itertools import combinations

def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    return board


def stop_game():
    exit()


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    users_choice = input(f"It's {player}'s turn, what coordinate will you use? ")
    print("\n")
    os.system('cls')
    while users_choice not in myDict.keys():
        if users_choice == "quit":
            print ("\n===== You chose to quit the game. SEE YOU SOON!!! =====\n")
            stop_game()
        print("\n")
        print_board(board)
        print("That's a wrong input, please use a combination of a letter and number for coordinates\n")
        users_choice = input(f"What coordinate will you use, {player}? ")
        print("\n")
        os.system('cls')
    else:

        row, col = myDict[users_choice][0], myDict[users_choice][1]
        while board[row][col] != ".":
            print("\n")
            print_board(board)
            print("That space has already been used, please select another\n")
            users_choice = input(f"What coordinate will you use, {player}? ")
            print("\n")
            os.system('cls')
            row, col = myDict[users_choice][0], myDict[users_choice][1]
    picked.append(users_choice)
    player_input.append(users_choice)
    temp=list(combinations(player_input, 2))
    for ele in temp:
        combos.append("".join(ele))
    return row, col
            

def get_ai_move(board):
    possible_input=list(myDict)
    for item in possible_input:
        if item in picked:
            possible_input.remove(item)
    ai_input=random.choice(possible_input)
    while count<3:
        picked.append(ai_input)
        return myDict[ai_input]
    else:
        nums=['1','2','3']
        letters=['A','B','C']
        possible_1=["A1A3","A1A2","A2A3","A3A1","A2A1","A3A2",
        "B1B3","B1B2","B2B3","B3B1","B2B1","B3B2", 
        "C1C3","C1C2","C2C3","C3C1","C2C1","C3C2"]
        possible_2=["A1B1","A1C1","B1C1","B1A1","C1A1","C1B1",
        "A2B2","A2C2","B2C2","B2A2","C2A2","C2B2"
        "A3B3","A3C3","B3C3","B3A3","C3A3","C3B3"]
        possible_3=["A1B2","A1C3","B2C3","B2A1","C3A1","C3B2",
        "C1B2","C1A3","A3B2","B2C1","A3C1","B2A3"]
        for word in combos:
            if word in possible_1:
                for y in nums:
                    if y not in word:
                        result = re.sub("[1-3]", y, word)
                result=result[0]+result[1]
                if result not in picked:
                    picked.append(result)
                    return myDict[result]
            elif word in possible_2:
                for y in letters:
                    if y not in word:
                        result = re.sub("[A-C]", y, word)
                result=result[0]+result[1]
                if result not in picked:
                    picked.append(result)
                    return myDict[result]
            elif word in possible_3:
                for y in nums:
                    for z in letters:
                        if y not in word and z not in word:
                            result = re.sub("[A-C]", z, word)
                            result = re.sub("[1-3]", y, result)
                result=result[0]+result[1]
                if result not in picked:
                    picked.append(result)
                    return myDict[result]
            else:
                picked.append(ai_input)
                return myDict[ai_input]



def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if player == "X":
        board[row][col] = "X"
        print("\n")
        print_board(board)
    elif player == "O":
        board[row][col] = "O"
        print("\n")
        print_board(board)


def has_won(board, player):
    """Returns True if player has won the game."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
        if (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
            return True
    return False


def is_full(board):
    """Returns True if board is full."""
    if "." not in board[0] and "." not in board[1] and "." not in board[2]:
        return True
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    c_1 = "1"
    c_2 = "2"
    c_3 = "3"
    r_1 = "A"
    r_2 = "B"
    r_3 = "C"
    print(3 * " " + c_1 + "   " + c_2 + "   " + c_3)
    print(r_1 + "  " + " | ".join(board[0][:3]))
    print(2 * " " + 3 * "-" + "+" + 3 * "-" + "+" + 3 * "-")
    print(r_2 + "  " + " | ".join(board[1][:3]))
    print(2 * " " + 3 * "-" + "+" + 3 * "-" + "+" + 3 * "-")
    print(r_3 + "  " + " | ".join(board[2][:3]))
    print("")


def print_result(winner,player_name):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if (winner == "X" or winner == "O") and player_name=="A.I.":
        print (f"===== Sorry, The {player_name} beated you! =====")
        stop_game()
    elif winner == None:
       print ("===== Nobody won, it's a tie ! =====")
       stop_game()
    else:
        print (f"===== Congrats *{player_name}*, you won the game! =====")
        stop_game()


def tictactoe_game(mode='HUMAN-HUMAN'):
    player_name_1=input("\n * Firstly type the first player's name:\n-> ")
    os.system('cls')
    while(player_name_1==""):
        player_name_1=input("\n * Empty name not available, so type the first player's name:\n-> ")
        os.system('cls')
    player_name_2=input("\n\n\n * Now type the second player's name:\n-> ")
    os.system('cls')
    while(player_name_2==""):
        player_name_2=input("\n * Emppt name not available, so type the second player's name:\n-> ")
        os.system('cls')
    while player_name_1==player_name_2:
        print("\n=========================================")
        print("\n* Players cannot have the same name *\n")
        player_name_2=input(" * Type the second player's name again:\n-> ")
        os.system('cls')
    while(player_name_2==""):
        player_name_2=input("\n * Emppt name not available, so type the second player's name:\n-> ")
        os.system('cls')
    board = init_board()
    is_full(board)
    print("\n")
    print_board(board)
    while has_won(board, "X") is False or has_won(board, "O") is False:
        row, col = get_move(board, player_name_1)
        mark(board, "X", row, col)    
        if has_won(board, "X") is True:
            print_result("X", player_name_1)
        if is_full(board) is True:
            print_result(None,None)

        row, col = get_move(board, player_name_2)
        mark(board, "O", row, col)  
        if has_won(board, "O") is True:
            print_result("O", player_name_2)
        if is_full(board) is True:
            print_result(None,None)
            
    
def tictactoe_game_2(mode='HUMAN-AI'):
    global count
    player_name=input("\n * Firstly type your name:\n-> ")
    os.system('cls')
    board = init_board()
    is_full(board)
    print("\n")
    print_board(board)
    while has_won(board, "X") is False or has_won(board, "O") is False:
        row, col = get_move(board, player_name)
        count+=1
        mark(board, "X", row, col) 
        if has_won(board, "X") is True:
            print_result("X", player_name)
        if is_full(board) is True:
            print_result(None,None)
        
        os.system('cls')
        print("Your opponent marked, now it's your turn!")
        row, col = get_ai_move(board)
        count+=1
        mark(board, "O", row, col)
        if has_won(board, "O") is True:
            print_result("O", "A.I.")
        if is_full(board) is True:
            print_result(None,None)


def main_menu():
    print ("=================================")
    print ("\n* Welcome to Tic-Tac-Toe game ! *\n")
    print ("=================================")
    print ("\nThere are two gamemodes to choose from:")
    print ("\t1. Player vs Player (Challenge a friend)")
    print ("\t2. Player vs A.I. (Try to beat your system)\n")
    print ("*IMPORTANT* You can also quit the game already by typing: 'quit' \n")
    

def start_game():
    user_menu= input ("Choose your match by typing the corresponding number, or you can quit:")
    if  (str(user_menu) == "1"):
      os.system('cls')
      print ("\nYou have selected a Player vs Player match. Let's  get started !:")
      tictactoe_game('HUMAN-HUMAN')
    elif (str(user_menu) == "2"):
      os.system('cls')
      print ("\nYou have selected a Player vs A.I. match. Let's  get started !:\n")
      tictactoe_game_2('HUMAN-AI')
    elif (str(user_menu) == "quit"):
      os.system('cls')
      print ("\n===== You chose to quit the game. SEE YOU SOON!!! =====\n")
      stop_game()
    else: 
     os.system('cls')
     main_menu()
     print ("\n* That is an invalid selection, please try again ! *\n")
     start_game()

myDict = {
        "A1": [0, 0],
        "A2": [0, 1],
        "A3": [0, 2],
        "B1": [1, 0],
        "B2": [1, 1],
        "B3": [1, 2],
        "C1": [2, 0],
        "C2": [2, 1],
        "C3": [2, 2]
    }
count=0
marks=["X","O"]
picked=[]
player_input=[]
combos=[]
main_menu()
start_game()
