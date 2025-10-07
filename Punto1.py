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

    #Peso del árbol 
    def peso(self):
        return self._contar_nodos(self.raiz)

    def contarNodos(self, nodo):
        if nodo is None:
            return 0
        total = 1  
        for hijo in nodo.hijos:
            total += self.contarNodos(hijo)
        return total

    #Altura del árbol
    def altura(self):
        return self.maxAltura(self.raiz)

    def maxAltura(self, nodo):
        if nodo is None:
            return 0
        if not nodo.hijos:
            return 1
        return 1 + max(self.maxAltura(hijo) for hijo in nodo.hijos)
    
#PRUEBA   
orden = int(input("Defina el orden del arbol: "))
arbol1 = Arbol(orden)
arbol1.crear_arbol()
print("Peso del arbol: ", arbol1.peso())
print("Orden del arbol: " , arbol1.orden)
print("Altura del arbol: " , arbol1.altura())
    


