from producto import *
#Variable para funcionar con cliente, Leer BBDD
disp = [Producto("stout", 4.5, 3), Producto("ipa", 3.75, 5), Producto("ale", 2.75, 8), Producto("pastry", 5, 4)]

#CLASE DIRECCION, el cliente prodrá guardar mas de una direccion
class Direccion:
    #___INIT___
    def __init__(self, calle, numero, lugar, cp, provincia, pais):
        self.__calle = calle
        self.__numero = numero
        self.__lugar = lugar
        self.__cp = cp
        self.__provincia = provincia
        self.__pais = pais

    #Get
    def get_direccion(self):
        return self.__calle, self.__numero, self.__lugar, self.__provincia, self.__cp, self.__pais

#CLASE CLIENTE
class Cliente:
    #__INIT__
    def __init__(self, nombre, mail = "", tlfn = 123456789):
        self.__nombre = nombre
        self.__mail = mail
        self.__tlfn = tlfn
        self.__direccion = []
        self.__cesta = [] #Dict or tuple?

    #Getters
    def get_cliente(self):
        print(f"{self.__nombre} {self.__tlfn}\n{self.__mail}\n")

    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        '''l = self.direccion.copy()
        print(f"\n\t Direccion de {self.get_nombre()}:")
        for i in l:
            i.get_direccion()'''
        print(f"\n\t Direccion de {self.get_nombre()}:")
        for i in self.__direccion:
            calle, numero, lugar, prov, cp , pais = i.get_direccion()
            print(f"C/ {calle} Nº: {numero}")
            print(f"{lugar}({prov}) {cp}")
            print(f"{pais}")
            print('\n')

    def get_cesta(self):
        return self.__cesta.copy()
            
    #Setters
    def add_producto(self, name, amount):
        i = 0
        while (name != disp[i].get_nombre()): #Podria cambiar a punteros o por index()
            i += 1
        p = Producto(disp[i].get_nombre(), disp[i].get_precio(), amount) #Arreglar lo del precio debido a que seria privado para el cliente pero solo podria verlo
        self.__cesta.append(p)

        disp[i].set_stock(disp[i].get_stock() - amount)

    def add_direccion(self):
        print("\tIntroduciendo los datos de la direccion del cliente:")
        calle = input("\tCalle: ")
        numero = input("\tNumero: ")
        lugar = input("\tPoblacion: ")
        cp = input("\tC.P.:")
        provincia = input("\tProvincia: ")
        pais = input("\tPais: ")

        self.__direccion.append(Direccion(calle, numero, lugar, cp, provincia, pais))

if __name__ == "__main__":

    c = Cliente("Chinook", "asdfg@asf.com", 687550062)

    c.get_cliente()

    print("*****")

    c.get_cesta()

    c.add_direccion()

    c.get_direccion()