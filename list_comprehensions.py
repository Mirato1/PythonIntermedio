def run():
    #squares = []
    #for i in range(1, 101):
    #   if i % 3 != 0:
    #        squares.append(i**2)

    #List Comprehension
    #Para cada i en el rango 1-100 voy a guardar la I**2
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)    

    #---------------------EJERCICIO-----------------------------------
    #Crear, con un list comprehension, una lista de todos los múltiplos
    #de 4 que a la vez también son múltiplos de 6 y de 9, hasta 5 dígitos



    number = [i for i in range(1, 100000) if i % 36 == 0]
    print(number)
    
    
    ejercicio = [i for i in range (100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]
    print (ejercicio)


if __name__ == '__main__':
    run()