def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Lucas", "lastname": "Giménez"}

    super_list = [
        {"firstname": "Lucas", "lastname": "Giménez"},
        {"firstname": "Yamy", "lastname": "Mouri"},
        {"firstname": "Nicolás", "lastname": "Chikahuala"},
        {"firstname": "Facu", "lastname": "Pérez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.1, 5.12, 5.14]
    }

    #Imprimir super_list completo
    for i in super_list:       
        for key, value in i.items():
            print(key, "-", value)
        print("♥" * 20)

        
    #Imprimir super_dict completo
    for key, value in super_dict.items():
        print(key, "-", value)



if __name__ == '__main__':
    run()