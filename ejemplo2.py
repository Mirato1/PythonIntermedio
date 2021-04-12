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
    print('😱 H A N G M A N --- G A M E 😱')
    print('')
    print(IMAGES[tries])
    print('')
    print('')
    print('')
    for i in hidden_word:
        print(i + " ", end="")
    print("\n")
    print('◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽')
    print('◽◽◽◽◽◽◽◽◽◽LETRAS REPETIDAS◽◽◽◽◽◽◽◽◽◽')
    for i in repeated_letters:
        print(i + " ", end="")
    print("\n")



def run():
    word = get_word()
    hidden_word = ['➖'] * len(word)
    repeated_letters = []
    tries = 0
    while True:
        board(tries, hidden_word, repeated_letters)
        letter = input("Ingresa una letra❗: ").strip().upper()
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
                print(f'💀 Perdiste ❗ La palabra correcta era {word}')
                break
        else:
            for idx in letter_idx:
                hidden_word[idx] = letter

            letter_idx = []
        
        try:
            hidden_word.index('➖')
        except ValueError:
            print('')
            print(f'😁 Felicidades 😁 Ganaste 🎉 La palabra es {word}')
            break        


if __name__ == '__main__':
    run()