import random
import os

def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [ line for line in f ]
    return data

def print_word(word, end=''):
    for letter in word:
        print(letter, end=end)
    print('\n')

def print_state(hanged_word, traced_word):
    os.system('clear')
    print('Tu estado:')
    print_word(hanged_word, end=' ')
    print('Tu palabra, considera como diferentes las letras tildadas:')
    print_word(traced_word, end=' ')

def read_letter():
    letter = input('Ingrese una letra: ').strip().upper()
    assert letter.isalpha(), 'Ingrese solo letras'
    assert len(letter) == 1, 'Ingrese solo una letra'
    return letter

def run():
    words = read_data('./archivos/data.txt')
    random_word = random.choice(words).strip().upper()
    random_word = [ letter for letter in random_word ]
    traced_word = [ '_' for letter in random_word ]
    _hanged_word = 'AHORCADO'
    hanged_word = [ '_' for letter in _hanged_word ]
    count = 0
    while count < len(_hanged_word):
        print_state(hanged_word, traced_word)
        letter = ''
        try:
            letter = read_letter()
        except AssertionError as ae:
            print(ae)
            input('presiona enter para continuar')
        if letter in random_word:
            traced_word = [ letter if letter == random_letter else traced_word[index]
                            for index, random_letter in enumerate(random_word) ]
        else:
            hanged_word[count] = _hanged_word[count]
            count += 1
        if '_' not in traced_word:
            print_state(hanged_word, traced_word)
            print('\n¡Ganaste! la palabra era', end=' ')
            print_word(random_word)
            break
    else:
        print_state(hanged_word, traced_word)
        print('\n¡Perdiste! la palabra era', end=' ')
        print_word(random_word)

if __name__ == '__main__':
    run()