#Clase de High order functions: Filter, Map y Reduce

def run():
    
    #Filtrar números impares de la lista sin filter
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]

    add = [i for i in my_list if i % 2 != 0]

    print(add)


    #Misma función pero usando Filter

    my_list_2 = [1, 4, 5, 6, 9, 13, 19, 21]

    odd = list(filter(lambda x: x%2 != 0, my_list_2))

    print(odd)

    #Retornar la misma lista elevada al cuadrado

    my_list_3 = [1, 2, 3, 4, 5]
    
    ejercicio = [i**2 for i in my_list_3]
    
    print(ejercicio)


    #Misma función pero usando Map

    my_list_4 = [1, 2, 3, 4, 5]

    squares = list(map(lambda x: x**2, my_list_4))

    print(squares)


    #Recorrer cada número de la lista y multiplicarlos.
    
    my_list_5 = [2, 2, 2, 2, 2]

    all_multiplied = 1

    for i in my_list_5:
        all_multiplied = all_multiplied * i

    print(all_multiplied)
    
    
    #Misma función usando Reduce
    #Para poder usar reduce
    from functools import reduce

    my_list_6 = [2, 2, 2, 2, 2]
    # A, b = 1° y 2° número de la lista,
    # después el B pasa a ser A y así sucesivamente
    all_multiplied_1 = reduce(lambda a, b:a * b, my_list_6)

    print(all_multiplied_1)



if __name__ == '__main__':
    run()