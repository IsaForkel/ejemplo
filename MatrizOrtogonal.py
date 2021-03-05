import NodoMatriz as Nod
class MOrtogonal():

    def __init__(self):
        self.Cabecera = None

    def Crear(self,filas,columnas,lista):
        RefArriba = Nod.Cajita(None)
        RefDerecha = Nod.Cajita(None)
        for i in range(1,filas+1):
            for j in range(1,columnas+1):
                nuevo = Nod.Cajita(lista.pop)
                nuevo.abajo = None
                nuevo.derecha = None
                if j == 1:
                    nuevo.derecha = None
                    if self.Cabecera == None:
                        self.Cabecera = nuevo
                    RefDerecha = nuevo
                else:
                    nuevo.izquierda = RefDerecha
                    RefDerecha.derecha = nuevo
                    RefDerecha = nuevo
                if i == 1:
                    nuevo.arriba = None
                    RefDerecha = nuevo
                else:
                    nuevo.arriba = RefArriba
                    RefArriba.abajo = nuevo
                    RefArriba = RefArriba.derecha
            RefArriba = self.Cabecera
            while RefArriba.abajo is not None:
                RefArriba = RefArriba.abajo

    def Buscar(self):
        return None

    def Eliminar(self,valor):
        inicio = self.Cabecera
        contador = 0
        while inicio is not None:
            derecha = inicio
            while derecha is not None:
                if valor == contador:
                    if derecha.arriba is not None:
                        if inicio.abajo is not None:
                            derecha.arriba.abajo = derecha.abajo
                            derecha.abajo.arriba = derecha.arriba
                        else:
                            derecha.arriba.abajo = derecha.abajo
                    else:
                        if derecha.abajo is not None:
                            derecha.abajo.arriba = derecha.arriba
                        else:
                            derecha.arriba.abajo = derecha.abajo
                derecha = derecha.derecha3
            contador = contador+1
            inicio = inicio.abajo

    def Comparar(self,valor):
        filas = 0
        inicio = self.Cabecera
        while inicio is not None:
            columnas = 0
            derecha = inicio
            while derecha is not None:
                if columnas == valor:
                    return True
                columnas = columnas+1
                derecha = derecha.derecha
            filas = filas+1
            inicio = inicio.abajo
        return False