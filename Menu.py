import xml.etree.ElementTree as ET
import Matriz
class Nodos:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
class Nodo2:
    def __init__(self,nombre,id,matriz):
        self.nombre = nombre
        self.id = id
        self.matriz = matriz
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None
        self.q = None
    
    def insertar(self,nodo):
        p = nodo
        p.siguiente = None
        if self.cabeza == None:
            self.cabeza = p
        else:
            self.q.siguiente = p
        self.q = p
    def pop(self):
        temp = ""
        if self.cabeza is not None:
            temp = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
        return temp
    def mostrar(self,nombre):
        temporal = self.cabeza
        while temporal is not None:
            if temporal.nombre == nombre:
                temporal.matriz.visualizar()
                break
            temporal = temporal.siguiente

    def Comparar(self, nombre,x,y):
        temporal = self.cabeza
        while temporal is not None:
            if temporal.nombre == nombre:
                print(temporal.matriz.Comparar(x,y))
                break
            temporal = temporal.siguiente
    def Eliminar(self, nombre,fila):
        temporal = self.cabeza
        while temporal is not None:
            if temporal.nombre == nombre:
                temporal.matriz.Eliminar(fila)
                break
            temporal = temporal.siguiente

class Menu:
    def __init__(self):
        self.lista = Lista()
        pass

    def menu(self):
        bandera = True
        while bandera:
            print("Menu")
            print("1.Leer Archivo")
            print("2.Buscar y Mostrar")
            print("3.Eliminar Fila")
            print("4.Comparar")
            print("5.Buscar")
            op = input("Seleccione la opcion")
            if(op is "1"):
                archivo = input("Ingrese el archivo")
                tree = ET.parse(archivo)
                root = tree.getroot()
                banderita = 0
                for elemento in root:
                    n = elemento.get('n')
                    m = elemento.get('m')
                    nombre = elemento.get("nombre")
                    datos = Lista()
                    for subelemento in elemento:
                        dato = subelemento.text
                        datos.insertar(Nodos(dato))
                    matriz = Matriz.MatrizOrtogonal()
                    matriz.Create(int(n),int(m),datos)
                    self.lista.insertar(Nodo2(nombre,banderita,matriz))
                    banderita = banderita+1
            elif(op is "2"):
                self.lista.mostrar(input("Ingrese el nombre: "))
            elif(op is "4"):
                self.lista.Comparar("Ejemplo",int(input("Fila1: ")),int(input("Fila2: ")))
                bandera = False
            elif(op is "5"):
                self.lista.Eliminar("Ejemplo",int(input("Fila:")))
                bandera = False
            elif(op is "6"):
                bandera = False
objeto = Menu()
objeto.menu()