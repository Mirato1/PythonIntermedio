def run():

    #Usando función lambda para realizar el ejercicio de palíndromos
    palindrome = lambda string: palabra == palabra [::-1]
    
    palabra = input("Ingrese una palabra: ")
    palabra = palabra.lower()
    palabra = palabra.replace(' ', '')

    if palindrome(palabra):
        print('Felicitaciones, es palíndromo')
    
    else:
        print('No es palíndromo')

if __name__ == '__main__':
    run()