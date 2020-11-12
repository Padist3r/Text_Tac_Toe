import random


def bot(string):
    """Randomly selects a place for the computers turn."""
    if string == "":
        return None
    else:
        r = random.randint(0, len(string) - 1)
        return string[r]


def check_win(string: str) -> str:
    """Takes the board string and converts it into lists that can be checked
    to determine a win, loose or draw"""
    game_state = [[], [], []]
    for j in range(0, len(string) - 1):
        if string[j] in "123456789XO-":
            if j < 11:
                game_state[0].append(string[j])
            elif 11 < j < 24:
                game_state[1].append(string[j])
            else:
                game_state[2].append(string[j])

    for line in game_state:
        if "X" not in line and "-" not in line:
            return "O"
        elif "O" not in line and "-" not in line:
            return "X"
    if game_state[0][0] == game_state[1][1] == game_state[2][2] == "X" or \
            game_state[0][2] == game_state[1][1] == game_state[2][0] == "X":
        return "X"
    elif game_state[0][0] == game_state[1][1] == game_state[2][2] == "O" or \
            game_state[0][2] == game_state[1][1] == game_state[2][0] == "O":
        return "O"
    elif game_state[0][0] == game_state[1][0] == game_state[2][0] == "X" or \
            game_state[0][1] == game_state[1][1] == game_state[2][1] == "X" or \
            game_state[0][2] == game_state[1][2] == game_state[2][2] == "X":
        return "X"
    elif game_state[0][0] == game_state[1][0] == game_state[2][0] == "O" or \
            game_state[0][1] == game_state[1][1] == game_state[2][1] == "O" or \
            game_state[0][2] == game_state[1][2] == game_state[2][2] == "O":
        return "O"
    else:
        return "Draw"


game_on = True
bot_board = "123456789"
board = " 1 | 2 | 3 \n 4 | 5 | 6 \n 7 | 8 | 9 "

print("Please press enter to begin --> ")
while game_on:
    user = input("-->")

    if user in bot_board and user != "":
        board = board.replace(user, "X", 1)
        bot_board = bot_board.replace(user, "", 1)

        # checks to see if the last game space has been taken
        if bot_board == "":
            pass
        else:
            bot1 = bot(bot_board)
            board = board.replace(bot1, "O", 1)
            bot_board = bot_board.replace(bot1, "", 1)

        # changes the board so it looks a bit nicer
        show_board = board
        for i in board:
            if i in "123456789":
                show_board = show_board.replace(i, "-", 1)
        print(show_board)
        # Checks to see if there is a winner
        check = check_win(show_board)
        if check == "X":
            print("X WINS!!")
            game_on = False
        elif check == "O":
            print("O Wins!!")
            game_on = False
        elif check == "DRAW":
            print("DRAW GAME!!")
            game_on = False
        # resets variables for the next turn
        try:
            del bot1
            del check
        except NameError:
            pass

    else:
        # If there is an incorrect input the board will be displayed and the
        # user asked for an input
        print(board)
        print("Please place an X in an appropriate place")
