class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []  

class Arbol:
    def __init__(self, orden):
        self.orden = orden
        self.raiz = None

    def crearArbol(self):
        dato = input("Ingrese el dato para la raíz: ")
        self.raiz = Nodo(dato)
        self.agregarHijos(self.raiz)

    def agregarHijos(self, nodo):
        while True:
            numHijos = int(input(f"Ingrese cuántos hijos tiene el nodo '{nodo.dato}' (máx {self.orden}): "))
            if 0 <= numHijos <= self.orden:
                break  
            print(f" Error: el número de hijos no puede ser mayor que {self.orden} ni tener un valor menor a 0.")

        for i in range(numHijos):
            datoHijo = input(f"Ingrese el dato del hijo {i + 1} de '{nodo.dato}': ")
            nuevoHijo = Nodo(datoHijo)
            nodo.hijos.append(nuevoHijo)

            preguntarMasHijos = input(f" '{datoHijo}' ¿tiene hijos? (s/n): ").lower()
            if preguntarMasHijos == 's':
                self.agregarHijos(nuevoHijo)


