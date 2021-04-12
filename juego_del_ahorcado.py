import os
import random

dict_dibujo = {0:'''
  +---+
  |   |
      |
      |
      |
      |
=========''', 1:'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 2:'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 3:'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 4:'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 5:'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 6:'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',}

def leer_palabra_aleatoria():

    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        palabra_aleatoria = random.choice( [palabra.lower().strip() for palabra in f]  )
    return palabra_aleatoria

def actualizar_blank_spaces(palabra, letra_tentativa, blank_spaces):
    
    blank_spaces = blank_spaces.split(' ')
    indices = list( filter( lambda x: letra_tentativa==x[1], list(enumerate(palabra)) ) )
    for indice in indices:
        blank_spaces[indice[0]] = indice[1].upper()
                
    blank_spaces = ' '.join(blank_spaces)
    numero_de_blank_spaces = blank_spaces.count('_')
    return blank_spaces, numero_de_blank_spaces

def juego():
    
    ## Leo la palabra ##
    palabra = leer_palabra_aleatoria()
    blank_spaces = ['_ ' for i in range(len(palabra))]
    blank_spaces = ''.join(blank_spaces)
    vidas = 6
    numero_de_blank_spaces = 1
    while vidas > 0 and numero_de_blank_spaces>0:
        
        # Interfaz y pido la letra #
        os.system('cls')
        print(dict_dibujo[vidas])
        print('Adivina la palabra!!!')
        print(f'Por ahora tienes {vidas} vidas.')
        print(blank_spaces)
        letra_tentativa = input('Introduce la letra que creas que pertenece a la plabara: ').lower()
        
        ## En caso de que no se digite una letra ##
        if letra_tentativa.isnumeric() or len(letra_tentativa)>1 or letra_tentativa.isalnum():
            print()
            print("Eh, tienes que introducir una (1) letra!!")
            vidas -= 1
            print("Lamento informarte que tienes una vida menos.")
            print()
        else:
            ## Descuento vida si es el caso ##
            if not (letra_tentativa in palabra):
                print()
                print("Escogiste la letra equivocada, tienes una vida menos")
                print()
                vidas -= 1
            ## Se actualizan los blank spaces ##
            blank_spaces, numero_de_blank_spaces = actualizar_blank_spaces(palabra, letra_tentativa, blank_spaces)
    
    if numero_de_blank_spaces==0:
        print()
        print('GANASTE, GRACIAS POR JUGAR!!!')
        print()
        print(f'Efectivamente la palabra era {palabra.upper()}')    
    else:
        print(dict_dibujo[vidas])
        print('Lamento decirte que perdiste, buena suerte en la proxima.')
        print(f'La palabra era {palabra.upper()}.')
        
        
if __name__ == '__main__':
    juego()