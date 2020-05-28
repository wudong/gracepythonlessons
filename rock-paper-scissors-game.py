import random
moves = ["r", "p", "s"]
player_wins = ["rs", "pr", "sp"]

while True:
    player_move = input("your move:")
    if player_move == "q":
        break
    computer_move = random.choice(moves)
    print("you:", player_move)
    print("me:", computer_move)
    if player_move == computer_move:
        print("TIE!!")
    elif player_move + computer_move in player_wins:
        print("YOU WIN!!")
    else:
        print("YOU LOSE!!")