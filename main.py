import random


def bot(string):
    if string == "":
        return None
    else:
        r = random.randint(0, len(string) - 1)
        return string[r]


def check_win(string):
    pass


game_on = True
bot_board = "123456789"
board = " 1 | 2 | 3 \n 4 | 5 | 6 \n 7 | 8 | 9 "

print("Please press enter to begin --> ")
while game_on:
    user = input("-->")

    if user in bot_board and user != "":
        board = board.replace(user, "X", 1)
        bot_board = bot_board.replace(user, "", 1)

        bot1 = bot(bot_board)
        print("Computer chooses...")
        board = board.replace(bot1, "O", 1)
        bot_board = bot_board.replace(bot1, "", 1)

        # print(board)
        show_board = board
        for i in board:
            if i in "123456789":
                show_board = show_board.replace(i, " ", 1)
        print(show_board)
        # resets bot1 for the next turn
        del bot1

    else:
        print(board)
        print("Please place an X in an appropriate place")
