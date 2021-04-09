DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

    #-----------------RETO---------------------#
    #•Crear las listas all_python_devs y all_Platzi_workers usando una
    # combinación de filter y map. 
    #•Crear la lista old_people y adults con list comprehensions. 
    #•Uno ejercicio aparte mío que retorne el nombre de los mayores a 25 años y que dominen Python. 

def run():
    
    #-------------------------EJERCICIO 1 -----------------------#

    print ('')
    print ('TODOS LOS TRABAJADORES QUE DOMINAN PYTHON')
    print ('')

    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    for worker in all_python_devs:
        print (worker)


    #-------------------------EJERCICIO 2 -----------------------#


    print ('')
    print ('*---*---*---*---*---*---*---*---*')
    print ('')
    print ('TODOS LOS TRABAJADORES DE PLATZI')
    print ('')

    all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))
    
    for worker in all_platzi_workers:
        print(worker)


    #-------------------------EJERCICIO 3 -----------------------#

    print ('')
    print ('*---*---*---*---*---*---*---*---*')
    print ('')
    print ('TODOS LOS TRABAJADORES MAYORES DE 18')
    print ('')

    adults = [worker["name"] for worker in DATA if worker ["age"] > 25]
    for worker in adults:
        print (worker)


    #-------------------------EJERCICIO 4 -----------------------#

    print ('')
    print ('*---*---*---*---*---*---*---*---*')
    print ('')
    print ('TODOS LOS TRABAJADORES MAYORES DE 70')
    print ('')

    old_people = [worker | {'old': worker['age'] > 70} for worker in DATA]
    print(old_people)
    
    #-------------------------EJERCICIO 5 -----------------------#

    print ('')
    print ('*---*---*---*---*---*---*---*---*')
    print ('')
    print ('MAYORES A 25 Y DOMINAN PYTHON')
    print ('')

    old_fifty = [worker["name"] for worker in DATA if worker["age"] > 25 and worker ["language"] == "python"]      
    for worker in old_fifty:
        print(worker)
    

if __name__ == '__main__':
    run()