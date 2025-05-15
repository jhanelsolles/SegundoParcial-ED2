class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        def _insertar(nodo, valor):
            if nodo is None:
                return Nodo(valor)
            if valor < nodo.valor:
                nodo.izquierda = _insertar(nodo.izquierda, valor)
            else:
                nodo.derecha = _insertar(nodo.derecha, valor)
            return nodo

        self.raiz = _insertar(self.raiz, valor)

    def buscar(self, valor):
        def _buscar(nodo, valor):
            if nodo is None:
                return False
            if nodo.valor == valor:
                return True
            elif valor < nodo.valor:
                return _buscar(nodo.izquierda, valor)
            else:
                return _buscar(nodo.derecha, valor)
        return _buscar(self.raiz, valor)

    def eliminar(self, valor):
        def _eliminar(nodo, valor):
            if nodo is None:
                return None
            if valor < nodo.valor:
                nodo.izquierda = _eliminar(nodo.izquierda, valor)
            elif valor > nodo.valor:
                nodo.derecha = _eliminar(nodo.derecha, valor)
            else:
                if nodo.izquierda is None:
                    return nodo.derecha
                elif nodo.derecha is None:
                    return nodo.izquierda
                temp = nodo.derecha
                while temp.izquierda:
                    temp = temp.izquierda
                nodo.valor = temp.valor
                nodo.derecha = _eliminar(nodo.derecha, temp.valor)
            return nodo
        self.raiz = _eliminar(self.raiz, valor)

    def inorden(self):
        def _inorden(nodo):
            return _inorden(nodo.izquierda) + [nodo.valor] + _inorden(nodo.derecha) if nodo else []
        return _inorden(self.raiz)
 
    # escribir la funcion def tio (self, t,s) y metodos adicionales 
    def encontrar_padre(self, valor):
        def _buscar_padre(nodo, padre):
            if nodo is None:
                return None
            if nodo.valor == valor:
                return padre
            if valor < nodo.valor:
                return _buscar_padre(nodo.izquierda, nodo)
            else:
                return _buscar_padre(nodo.derecha, nodo)
        return _buscar_padre(self.raiz, None)

    def son_hermanos(self, valor1, valor2):
        padre1 = self.encontrar_padre(valor1)
        padre2 = self.encontrar_padre(valor2)
        return padre1 is not None and padre1 == padre2 and valor1 != valor2

    def tio(self, t, s):
        if not self.buscar(t) or not self.buscar(s):
            return False

        padre_s = self.encontrar_padre(s)
        if padre_s is None or padre_s.valor == t:
            return False

        abuelo_s = self.encontrar_padre(padre_s.valor)
        if abuelo_s is None:
            return False

        return self.son_hermanos(t, padre_s.valor)
