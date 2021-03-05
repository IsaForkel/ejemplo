import Nodo
class MatrizOrtogonal():

    def __init__(self):
        self.cabeza = None
        self.graph = None

    def Create(self,n,m,cola):
        rd = None
        ra = None
        for i in range(1,n+1):
            for j in range(1,m+1):
                nuevo = Nodo.Nodox(cola.pop())#Dato
                nuevo.siguiente = None
                nuevo.abajo = None
                if j == 1:
                    nuevo.anterior = None
                    if self.cabeza == None:
                        self.cabeza = nuevo
                    rd = nuevo
                else:
                    nuevo.anterior = rd
                    rd.siguiente = nuevo
                    rd = nuevo
                if i == 1:
                    nuevo.arriba = None
                    rd = nuevo
                else:
                    nuevo.arriba = ra
                    ra.abajo = nuevo
                    ra = ra.siguiente
            ra = self.cabeza
            while ra.abajo != None:
                ra = ra.abajo

    def visualizar(self):
        inicio = self.cabeza
        cadena = ""
        while inicio!= None:
            iteracion = inicio
            while iteracion != None:
                cadena += " "+iteracion.dato+" "
                iteracion = iteracion.siguiente
            print(cadena)
            cadena = ""
            inicio = inicio.abajo

    def Comparar(self,x,x2):
        retorno = "Falso"
        inicio = self.cabeza
        contador = 1
        iteracion1 = None
        iteracion2 = None
        while inicio != None:
            if contador == x:
                iteracion1 = inicio
            if contador == x2:
                iteracion2 = inicio
            contador = contador+1
            inicio = inicio.abajo

        if iteracion1 != None and iteracion2 != None:
            valor = iteracion1
            valor2 = iteracion2
            while valor is not None:
                if valor.dato == valor2.dato:
                    print(valor.dato,valor2.dato)
                    retorno = "Verdadero"
                else:
                    retorno = "Falso"
                    return retorno
                valor = valor.siguiente
                valor2 = valor2.siguiente

        return retorno

    def Eliminar(self,eliminar):
        inicio = self.cabeza
        contador = 1
        while inicio != None:
            if contador == eliminar:
                j = inicio
                while j != None:
                    if j.arriba != None:
                        j.arriba.abajo = j.abajo
                        j.abajo.arriba = j.arriba
                    else:
                        if j.abajo != None:
                            j.abajo.arriba = j.arriba
                        else:
                            self.cabeza == None
                    j = j.siguiente
            contador = contador+1
            inicio = inicio.abajo
        self.visualizar()

    def iteracion(self):
        fila1 = 1
        inicio = self.cabeza
        while inicio.abajo != None:
            fila2 = fila1+1
            inicio2 = inicio.abajo
            while inicio2 != None:
                if self.Comparar(fila1,fila2):
                    self.Eliminar(fila2)
                fila2 = fila2+1
                inicio2 = inicio2.abajo
                
            


