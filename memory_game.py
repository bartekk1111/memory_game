import os
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_board(height, width):
    GAME_BOARD = [["#"] * height for i in range(width)]
    board_size = height * width
    quantity_of_letters = int(board_size / 2)
    letters = []
    for i in range(0,quantity_of_letters):
        letter = random.choice(alphabet)
        if letter not in letters:
            letters.append(letter)
    letters = letters * 2
    print(letters)
    print(GAME_BOARD)
    letter_index = 0
    for i in range(0, len(GAME_BOARD)):
        for j in range(0, len(GAME_BOARD[i])):
            GAME_BOARD[i][j] = letters[letter_index]
            letter_index += 1

    # for i in range(0,2):
    #     random_letter = random.choice(letters)
    
    
        

        # for h in range(0,height):
        #     for w in range(0,width):
        #         GAME_BOARD[h][w] = random.choice(alphabet)
    return GAME_BOARD


def generate_player_board(height, width):
    PLAYER_BOARD = [["#"] * height for i in range(width)]
    return PLAYER_BOARD

def main():
    height = 5
    width = 4
    GAME_BOARD = generate_board(height, width)
    PLAYER_BOARD = generate_player_board(height, width)
    print(GAME_BOARD)
    print(PLAYER_BOARD)

if __name__ == "__main__":
    main()