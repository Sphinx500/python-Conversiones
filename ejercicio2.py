class Sumatoria:
    def __init__(self):
        self.tupla_valores=()
        self.val1 = float(input("Ingrese valor 1: "))
        self.val2 = float(input("Ingrese valor 2: "))
        self.val3 = float(input("Ingrese valor 3: "))
        self.val4 = float(input("Ingrese valor 4: "))
        self.val5 = float(input("Ingrese valor 5: "))
        self.val6 = float(input("Ingrese valor 6: "))
        self.tupla_valores = self.val1, self.val2, self.val3, self.val4, self.val5, self.val6

    def __str__(self):
        print("---------------------")
        return print("la tupla es: ", str(self.tupla_valores))

    def operaciones(self):
        nueva_lista = list(self.tupla_valores)
        print("---------------------")
        print("La nueva lista es: ", nueva_lista)
        print("---------------------")
        promedio = int(sum(nueva_lista) / len(nueva_lista))
        print("El promedio es: ", promedio)
        nuevo_dato = nueva_lista.append(promedio)
        print("Agregamos el promedio como elemento a la lista: ")
        print(nueva_lista)


suma = Sumatoria()
suma.__str__()
suma.operaciones()
