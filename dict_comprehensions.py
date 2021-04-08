def run():

    #Lista de los primeros 100 números naturales elevados al cubo
    dicts = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(dicts)
    
    #Reto: Crear, un diccionario cuyas llaves sean los 1000 primeros
    #números naturales con sus raíces cuadradas como valores.

    dicts_raiz = {i: i**0.5 for i in range(1, 1001)}   
    print (dicts_raiz)





if __name__ == '__main__':
    run()
