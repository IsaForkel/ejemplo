import xml.etree.ElementTree as ET

class Nodo:
    def __init__(self):
        self.dato = None
        self.siguiente = None


class Lista:
    def __init__(self):
        self.cabeza = None
        self.q = None
    
    def insertar(self, dato):
        p = Nodo()
        p.dato = dato
        p.siguiente = None
        if self.cabeza == None:
            self.cabeza = p
        else:
            self.q.siguiente = p
        self.q = p

class Menu:
    def __init__(self):
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
                datos = Lista()
                for subelemento in elemento:
                    dato = subelemento.text
                    datos.insertar(dato)
                inicioDatos = datos.cabeza

                #aqui pone tu codigo Matriz(n,m,inicioDatos)
                
        elif(op is "2"):
            pass
        elif(op is "4"):
            pass
        elif(op is "5"):
            pass
        elif(op is "6"):
            pass
