#--
#----version 2.0 - Shop @ TorresEspinosa,JoseAntonio----
#---

from cliente import *

#Posible funcion leer productos disponibles

#Func. control existencias, EVO
def existe_stock(name, c):
    check = False
    #Recorre datos
    for i in disp:
        #si hay coincidencia hay stock
        if name == i.get_nombre():
            if c < i.get_stock():
                check = True
                break
            else:
                print(f"\t-> Solo quedan {i.get_stock()}")
    return check

def existe(name):
    check = False
    #Recorre datos
    for i in disp:
        #si hay coincidencia existe
        if name == i.get_nombre():
            check = True
            break
    return check


#Func. comprar, EVO
def comprar (c, name_product):
    #Comprueba cantidad negariva
    try:
        x = int(input("\t-> Que cantidad?\n"))
        if x < 0:
            raise ValueError("ERROR. Cantidad negativa!")
        else:
            if existe_stock(name_product, x): #Comprueba si hay stock
                c.add_producto(name_product, x)
            #Posible reiteracion para volver a preguntar cantidad
    except ValueError as e:
        print(e) #Si se retornara el error podriamos saltarnos mediante un control en 'MAIN' la siguiente función que se ejecutaria 'finalizar()'

#Func. finalizar, EVO
def get_disponibles():
    #Recorre datos
    for i in disp:
        #si hay stock lo muestra
        if i.get_stock() > 0:
            print(f"\t{i.get_nombre()} {i.get_precio()}€")

def pagar(c):
    total = 0 #Posible retrurn para funcion de pago

    #HEAD
    print("--------------------------------------------------------------------------------------")
    print("Producto \t\t Cantidad \t\t Precio \t\t Valor")
    print("--------------------------------------------------------------------------------------")

    #PRODUCTOS
    #recorre cesta
    for i in c.get_cesta():
            #Calcula coste y total
            coste = i.get_stock() * i.get_precio()
            total += coste
            #imprime desglose
            print( i.get_nombre() + " \t\t\t " + str(i.get_stock()) + " \t\t\t " + str(i.get_precio()) + " € \t\t\t " + str(coste) + " €" )
    
    #TOTAL - anteriormente calculado, calculo de valores^
    print("--------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t TOTAL \t\t\t" + str(total) + " €")

def finalizar():
    check = input("-> Desea algo mas Y/N? ")
    if check.upper() == 'Y':
        get_disponibles()
        return True
    else:
        return False


#-------------   
# --- MAIN ---
#-------------

#Posible funcion leer stock o productos disponibles
disp = [Producto("stout", 3, 4.5), Producto("ipa", 5, 3.75), Producto("ale", 8, 2.75), Producto("pastry", 4, 5)]

#Función de entrada/login
name = input("\n\t-> Bienvenid@! Cual es su nombre: ")
print(f"\t{name}, estos son nuestros productos de hoy:\n")
c = Cliente(name)

get_disponibles()


#LOOP_PEDIDO
control = True #Control para while
while control:
    name_product = input("\n\t-> Que desea?\n")
    #Controla existencia de pedido
    try:
        if not existe(name_product): #Realmente seria existe_producto, aunque el cliente solo veria lo que existe
            raise ValueError("ERROR. Introduzca un producto valido.\n")
        else:
            #Si existe, se realiza el servicio
            comprar(c, name_product) 
            #Pregunta para finalizar servicio, controla salir del bucle infinito
            control = finalizar()
    except ValueError as e:
        print(e)

#Si acaba servicio, muestra la cuenta
pagar(c)

print("\n\t-> Gracias!")#Posible funcion de pago'''