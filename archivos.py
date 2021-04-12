# "r" = Sólo lectura
# "r+"= Lectura y escritura
# "w" = Sólo escritura, sobreescribe el archivo si existe y crea uno si no.
# "w+"= Escritura y lectura. Sobreescribe el archivo si existe sino crea uno.
# "a" = Añadido (agregar contenido). Crea el archivo si éste no existe
# "a+"= Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.


def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f: 
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Nicolás", "Miguel", "Pepe", "Lucas"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    write()


if __name__ == "__main__":
    run()