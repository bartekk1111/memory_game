import os
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_board(height, width):
    GAME_BOARD = [["#"] * height for i in range(width)]
    for h in range(0,height):
        for w in range(0,width):
            GAME_BOARD[h][w] = random.choice(alphabet)
    return GAME_BOARD


def generate_player_board(height, width):
    PLAYER_BOARD = [["#"] * height for i in range(width)]
    return PLAYER_BOARD

def main():
    height = 5
    width = 5
    GAME_BOARD = generate_board(height, width)
    PLAYER_BOARD = generate_player_board(height, width)
    print(GAME_BOARD)
    print(PLAYER_BOARD)

if __name__ == "__main__":
    main()