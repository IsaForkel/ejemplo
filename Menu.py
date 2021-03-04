import xml.etree.ElementTree as ET
import MatrizOrtogonal as MO
class Nodo:
    def __init__(self):
        self.dato = None
        self.siguiente = None
        self.matriz
class Nodo2:
    def __init__(self,nombre,id,matriz):
        self.nombre = nombre
        self.id = id
        self.matriz = matriz
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

class Menu:
    def __init__(self):
        self.lista = Lista()
        pass

    def menu(self):

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
            for elemento in root:
                n = elemento.get('n')
                m = elemento.get('m')
                nombre = elemento.get("nombre")
                datos = Lista()
                for subelemento in elemento:
                    dato = subelemento.text
                    datos.insertar(Nodo())
                objeto = MO.MOrtogonal()
                objeto.Crear(n,m,datos)
                self.lista.insertar(None,Nodo2(1,nombre,objeto))
                #aqui pone tu codigo Matriz(n,m,inicioDatos)
                
        elif(op is "2"):
            pass
        elif(op is "4"):
            pass
        elif(op is "5"):
            pass
        elif(op is "6"):
            pass
