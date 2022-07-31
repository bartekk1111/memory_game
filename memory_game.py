import os
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_alphabet_board(height, width):
    board = []
    letters = random.sample(alphabet, (width * height) // 2) * 2
    print(letters)

    for column_index in range(height):
        column = []
        for row_index in range(width):
            letter = random.choice(letters)
            column.append(letter)
            letters.remove(letter)
        board.append(column)
    return board
        
def generate_player_board(height, width):
    PLAYER_BOARD = [["#"] * width for i in range(height)]
    return PLAYER_BOARD

def main():
    height = 4
    width = 3
    GAME_BOARD = generate_alphabet_board(height, width)
    PLAYER_BOARD = generate_player_board(height, width)
    print(GAME_BOARD)
    print(PLAYER_BOARD)

if __name__ == "__main__":
    main()