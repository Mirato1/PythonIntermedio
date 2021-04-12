# Utiliza las palabras clave TRY, EXCEPT y RAISE para elevar un error si el
# usuario ingresa un número negativo en nuestro programa de divisores 

def divisors(num):
    divisors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    
    return divisors

def run():
    while True:
        try:
            num = int(input('Ingresa un número: '))
            if num < 0 or num == 0:
                raise ValueError
            print(divisors(num))
            print("Terminó mi programa")
            break
        except ValueError:
            print("Debes ingresar un entero positivo")


if __name__ == "__main__":
    run()