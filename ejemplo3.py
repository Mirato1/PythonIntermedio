import random
import os

def run():
    def normalize(s): # It removes the accents of a string
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s

    words = []
    with open('./archivos/data.txt', 'r', encoding='utf-8') as file: # Here we get the words from the file and make a list
        for line in file:
            words.append(line.strip().upper())

    the_word = random.choice(words).upper() #Here we make the '_' list according to the random selected word
    the_secret_word = ['_' for letter in the_word]
    keep_trying = True






    lifes = 7
    points = 0
    while keep_trying:
        os.system('cls') #This line cleans the screen in every try

        if lifes == 7: #Here starts the art
            print('''
 +----+
 |    |
      |
      |
      |
      |
=========''')
        elif lifes == 6:
            print('''
 +----+
 |    |
 O    |
      |
      |
      |
=========''')
        elif lifes == 5:
            print('''
 +----+
 |    |
 O    |
 |    |
      |
      |
=========''')
        elif lifes == 4:
            print('''
 +----+
 |    |
 O    |
/|    |
      |
      |
=========''')
        elif lifes == 3:
            print('''
 +----+
 |    |
 O    |
/|\   |
      |
      |
=========''')
        elif lifes == 2:
            print('''
 +----+
 |    |
 O    |
/|\   |
/     |
      |
=========''')
        elif lifes == 1:
            print('''
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
=========''')
        elif lifes == 0:
            print('''
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
    =====''')




        print(the_word)
        print(f'Points: {points}')

        you_got_it = False #This is made to lose life when you where wrong

        printable_secret_word = ''.join(the_secret_word) #It's the random selected word but like this ______ and it's being updated
        if printable_secret_word == the_word: #This is the win check
            print('''
 +----+
      |
      |
\O/   |
 |    |
/ \   |
=========''')
            print('🏆 !Victory¡ 🏆')
            choice = input('Press X to play again, press any other key to quit\n').upper()
            if choice == 'X':
                lifes = 7
                the_word = random.choice(words)
                the_secret_word = ['_' for letter in the_word]
                continue
            else:
                break
        print(printable_secret_word)


        try: #This 'try' improves performance
            your_letter = normalize(input('\nType a letter: ').upper())
            assert your_letter.isalpha(), input('A letter please, PRESS A KEY TO CONTINUE')
            assert len(your_letter) == 1, input('1 letter please, PRESS A KEY TO CONTINUE')
        except AssertionError as e:
            print(e)
            continue


        for i in range(len(the_word)): #This is the check for every input
            for l in range(len(the_word)):
                the_letter = normalize(the_word[l])
                if your_letter == the_letter:
                    if your_letter == the_secret_word[l]:
                        you_got_it = True
                        continue
                    else:
                        the_secret_word[l] = the_word[l]
                        points += 100
                        you_got_it = True
                        continue


        if you_got_it == False: #This is the life check
            lifes -= 1
            if lifes == -1:
                print(f'The word was {the_word}')
                choice = input('☠ Press X to play again, press any other key to quit ☠').upper()
                if choice == 'X':
                    lifes = 7
                    the_word = random.choice(words)
                    the_secret_word = ['_' for letter in the_word]
                    continue
                else:
                    break
            input('You lose one life, PRESS A KEY TO CONTINUE')

                

if __name__ == '__main__':
    run()