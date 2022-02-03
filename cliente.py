from producto import *
#Variable para funcionar con cliente
disp = [Producto("stout", 4.5, 3), Producto("ipa", 3.75, 5), Producto("ale", 2.75, 8), Producto("pastry", 5, 4)]

class Direccion:
    def __init__(self):
        pass

class Cliente:
    def __init__(self, nombre, mail = "", tlfn = 123456789):
        self.nombre = nombre
        self.mail = mail
        self.tlfn = tlfn
        self.direccion = []
        self.cesta = [Producto("stout", 5, 10)] #Dict or tuple?

    def get_cliente(self):
        print(f"{self.nombre} {self.tlfn}\n{self.mail}\n")
    
    def get_cesta(self):
        for i in range(0,len(self.cesta)):
            print(f"{self.cesta[i].get_nombre()} {self.cesta[i].get_precio()}€")
    
    def add_producto(self, name, amount):
        i = 0
        while (name != disp[i].get_nombre()): #Podria cambiar a punteros o por index()
            i += 1
        p = Producto(disp[i].get_nombre(), disp[i].get_precio(), amount) #Arreglar lo del precio debido a que seria privado para el cliente pero solo podria verlo
        print(f"{disp[i].get_nombre()} {disp[i].get_precio()} {disp[i].get_stock()}")
        self.cesta.append(p)

        print(disp[i].get_producto())

        x = disp[i].get_stock() - amount
        print(f"-> Stock antes: {disp[i].get_stock()}")
        disp[i].set_stock(x)
        print(f"-> Stock despues: {disp[i].get_stock()}")




    


'''#Prueba Cliente
c = Cliente("Chinook", "asdfg@asf.com", 687550062)

c.get_cliente()

print("*****")

c.get_cesta()#'''



#----Futuro MAIN (shop.py)----
#Func. control existencias, EVO
def existe_stock():
    return True

#Func. comprar, EVO
def comprar (c, name_product):
    #Comprueba stock
    try:
        x = int(input("\t-> Que cantidad?\n"))
        if x < 0:
            raise ValueError("ERROR. Cantidad negativa!")
        else:
            if existe_stock(): #Comprueba valor correcto
                c.add_producto(name_product, x)
            '''else:
                if x > stock.get(name): 
                    print("\t-> Solo quedan " + str(stock.get(name)) + " " + name + "\n") #Posible reiteracion para volver a preguntar cantidad'''
    except ValueError as e:
        print(e) #Si se retornara el error podriamos saltarnos mediante un control en 'MAIN' la siguiente función que se ejecutaria 'finalizar()'

#-------------   
# --- MAIN ---
#-------------

#Posible funcion leer stock o productos disponibles
#disp = [Producto("stout", 3, 4.5), Producto("ipa", 5, 3.75), Producto("ale", 8, 2.75), Producto("pastry", 4, 5)]

#Función de entrada/login
name = input("\n\t-> Bienvenid@! Cual es su nombre: ")
print(f"\t{name}, estos son nuestros productos de hoy:\n")
c = Cliente(name)

#Funcion mostrar productos
for i in range(0,len(disp)):
    print(f"\t{disp[i].get_nombre()} {disp[i].get_precio()}€")


#LOOP_PEDIDO
control = True #Control para while
while control:
    name_product = input("\n\t-> Que desea?\n")
    #Controla existencia de pedido
    try:
        if not existe_stock(): #Realmente seria existe_producto, aunque el cliente solo veria lo que existe
            raise ValueError("ERROR. Introduzca un producto valido.\n")
        else:
            #Si existe, se realiza el servicio
            comprar(c, name_product) 
            #Pregunta para finalizar servicio, controla salir del bucle infinito
            control = False #finalizar_servicio()
    except ValueError as e:
        print(e)

    

#Si acaba servicio, muestra la cuenta
#mostrar_cesta(cesta)

print("\n\t-> Gracias!")#Posible funcion de pago'''