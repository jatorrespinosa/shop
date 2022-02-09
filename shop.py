#--
#----version 2.0 - Shop @ TorresEspinosa,JoseAntonio----
#---

from cliente import *

clientes = []

#Posible funcion leer productos disponibles

#Func. control existencias, EVO
def existe_stock(name, x = 1):
    check = False
    #Recorre datos
    for i in disp:
        #si hay coincidencia hay stock
        if name == i.get_nombre():
            if x <= i.get_stock():
                check = True
                break
            else:
                if i.get_stock() == 0:
                    print(f"\t-> Se acabo el stock de {i.get_nombre()}")
                else:
                    print(f"\t-> Solo quedan {i.get_stock()}")
    return check

'''def existe(name, lista):
    check = False
    #Recorre datos
    for i in lista:
        #si hay coincidencia existe
        if name == i.get_nombre():
            check = True
            break
    return check'''

def get_disponibles():
    print('\n')
    #Recorre datos
    for i in disp:
        #si hay stock lo muestra
        if i.get_stock() > 0:
            print(f"\t{i.get_nombre()} {i.get_precio()}€")

def add_producto(c,name_product, amount):
    i = buscar_id(name_product, disp)
    p = Producto(name_product, disp[i].get_precio(), amount) #Arreglar lo del precio debido a que seria privado para el cliente pero solo podria verlo
    c.add_producto(p)
    #Func. quita stock cuando se pague!!
    disp[i].set_stock(disp[i].get_stock() - p.get_stock())

    #--- BORRAR P!!! --- Hacer funcion del que cantidad de productos descienda!!!!

    

#Func. comprar, EVO
def comprar (c):
    #LOOP_PEDIDO
    control = True #Control para while
    while control:
        print("--------------------------------------------------------------------------------------")
        print("     COMPRA")
        print("--------------------------------------------------------------------------------------\n")
        print(f"\t{c.get_nombre()}, estos son nuestros productos de hoy:")
        get_disponibles()
        name_product = input("\n[EXIT 'Q'] -> Que desea? ")

        if name_product.upper() == 'Q':#controla salir del bucle infinito
            control = False
        else:
            #Controla existencia de pedido
            try:
                if not existe(name_product, disp): #aunque el cliente solo veria lo que existe
                    raise ValueError("ERROR. Introduzca un producto valido.\n")
                else:
                    #Comprueba cantidad negariva
                    try:
                        if existe_stock(name_product):
                            x = int(input("\t-> Que cantidad?\n"))
                            if x <= 0:
                                raise ValueError("ERROR. Cantidad erronea!")
                            else:
                                if existe_stock(name_product, x): #Comprueba si hay stock
                                    add_producto(c, name_product, x)
                                #Posible reiteracion para volver a preguntar cantidad
                    except ValueError as e:
                        print(e) #Si se retornara el error podriamos saltarnos mediante un control en 'MAIN' la siguiente función que se ejecutaria 'finalizar()'
            except ValueError as e:
                print(e)


def mostrar_cesta(c):
    total = 0 #Posible retrurn para funcion de pago

    #HEAD
    print("--------------------------------------------------------------------------------------")
    print("     CESTA DE COMPRA")
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
    print("\t\t\t\t\t\t TOTAL \t\t\t" + str(total) + " €\n")

def opciones():
    print("--------------------------------------------------------------------------------------")
    print("     MENU")
    print("--------------------------------------------------------------------------------------")
    print("1 - Seguir Comprando")
    print("2 - Cambiar Cesta")
    print("3 - Vaciar Cesta")
    print("4 - Ver Cesta")
    print("5 - Ver Productos")
    print("6 - Salir")
    print("*****")
    print("7 - Guardar Cliente")
    print("8 - añadir stock")
    print("9 - cambiar precio")
    print("10 - Ver Pendientes")
    print("11 - Ver Almacen")
    print("12 - Limpiar Almacen")

def login():
    pass

#Fuc. finalinzar, EVO guardar cliente, si no se ha comprado no reservar productos, guardar historial de compra
def salir(c):
        return False


#-------------   
# --- MAIN ---
#-------------

#Posible funcion leer stock o productos disponibles
disp = [Producto("stout",  4.5, 3), Producto("ipa", 3.75, 5), Producto("ale", 2.75, 8), Producto("pastry", 5, 4)]

menu = {
    "1" : comprar,
    "4" : mostrar_cesta,
    "6" : salir
}

'''"2" : cambiar_cesta,
    "3" : vaciar_cesta,
    "5" : pagar,
    
    "7" : guardar_cliente,
    "8" : añadir_stock,
    "9" : cambiar_precio,
    "10" : mostrar_pendientes,
    "11" : mostrar_almacen,
    "12" : limpiar_almacen,'''

#Función de entrada/login
name = input("\n\t-> Bienvenid@! Cual es su nombre: ")
c = Cliente(name)

#Posible funcion leer base de datos

check = True
while check:
    try:
        opciones()
        accion = input("\n\t-> Que desea hacer? Introduzca codigo: \n")
        if int(accion) < 1 or int(accion) > 12:
            raise ValueError("ERROR. Codigo incorrecto!")
        if accion == '6': #Controla salir cliente
            f = menu[accion]
            check = f(c) #Salir 'check = False'
        else:
            f = menu[accion]
            f(c)
    except ValueError as e:
        print(e)
    
    #pasarela de pago

print("\n\t-> Gracias!")#Posible funcion de pago'''

#ERROR. al pedir algo que no queda en stock para que no acepte el nombre del producto y siga pidiendo otro