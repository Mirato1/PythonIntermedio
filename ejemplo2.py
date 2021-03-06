import random
import os

IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
        |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
    |   |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''','''
    ''']

def get_word():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as data_file:
        for line in data_file:
            words.append(line.strip().upper())
    return random.choice(words)

def board(tries, hidden_word, repeated_letters):
    clear = lambda: os.system('cls')
    clear()
    print('馃槺 H A N G M A N --- G A M E 馃槺')
    print('')
    print(IMAGES[tries])
    print('')
    print('')
    print('')
    for i in hidden_word:
        print(i + " ", end="")
    print("\n")
    print('鈼解椊鈼解椊鈼解椊鈼解椊鈼解椊鈼解椊鈼解椊鈼解椊鈼解椊鈼解椊鈼解椊鈼解椊鈼解椊鈼解椊')
    print('鈼解椊鈼解椊鈼解椊鈼解椊鈼解椊LETRAS REPETIDAS鈼解椊鈼解椊鈼解椊鈼解椊鈼解椊')
    for i in repeated_letters:
        print(i + " ", end="")
    print("\n")



def run():
    word = get_word()
    hidden_word = ['鉃?'] * len(word)
    repeated_letters = []
    tries = 0
    while True:
        board(tries, hidden_word, repeated_letters)
        letter = input("Ingresa una letra鉂?: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"
        
        letter_idx = []
        for idx in range(len(word)):
            if word[idx] == letter:
                letter_idx.append(idx)
        repeated_letters.append(letter)

        if len(letter_idx) == 0:
            tries += 1
            if tries ==7:
                board(tries, hidden_word, repeated_letters)
                print('')
                print(f'馃拃 Perdiste 鉂? La palabra correcta era {word}')
                break
        else:
            for idx in letter_idx:
                hidden_word[idx] = letter

            letter_idx = []
        
        try:
            hidden_word.index('鉃?')
        except ValueError:
            print('')
            print(f'馃榿 Felicidades 馃榿 Ganaste 馃帀 La palabra es {word}')
            break        


if __name__ == '__main__':
    run()