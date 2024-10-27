import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class Arbol:
    def __init__(self):
        # Constructor del árbol
        self.raiz = None

    def __del__(self):
        # Destructor del árbol
        self._destruir_recursivo(self.raiz)
        print("El árbol ha sido destruido.")

    def _destruir_recursivo(self, nodo_actual):
        # Método auxiliar para destruir el árbol recursivamente
        if nodo_actual:
            self._destruir_recursivo(nodo_actual.izquierdo)
            self._destruir_recursivo(nodo_actual.derecho)
            nodo_actual.izquierdo = None
            nodo_actual.derecho = None

    def esVacio(self):
        # Comprueba si el árbol está vacío
        return self.raiz is None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)

    def graficar(self):
        if self.esVacio():
            print("El árbol está vacío.")
            return

        fig, ax = plt.subplots()
        self._graficar_recursivo(self.raiz, ax, 0, 0, 100, 50)
        ax.axis('off')
        plt.show()

    def _graficar_recursivo(self, nodo_actual, ax, x, y, dx, dy):
        if nodo_actual:
            ax.text(x, y, str(nodo_actual.valor), fontsize=12, ha='center', va='center',
                    bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.5'))

            # Graficar el nodo izquierdo
            if nodo_actual.izquierdo:
                ax.plot([x, x - dx], [y - 5, y - dy], 'k-')
                self._graficar_recursivo(nodo_actual.izquierdo, ax, x - dx, y - dy, dx / 2, dy)

            # Graficar el nodo derecho
            if nodo_actual.derecho:
                ax.plot([x, x + dx], [y - 5, y - dy], 'k-')
                self._graficar_recursivo(nodo_actual.derecho, ax, x + dx, y - dy, dx / 2, dy)

# Ejemplo de uso
arbol = Arbol()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(12)
arbol.insertar(18)

# Verifica si el árbol está vacío
print("¿El árbol está vacío?", arbol.esVacio())

# Graficar el árbol
arbol.graficar()
