#Ejercicio de clase -carrito- Prog. Av. Python v1 idea shop
# TorresEspinosa,JoseAntonio

cesta = {
    "stout" : 0,
    "ipa" : 0,
    "ale" : 0,
    "pastry" : 0
}
stock = {
    "stout" : 3,
    "ipa" : 5,
    "ale" : 8,
    "pastry" : 4
}
precio = {
    "stout" : 4.5,
    "ipa" : 3.75,
    "ale" : 2.75,
    "pastry" : 5
}

def add_producto(name, amount):
    cesta[name] += amount
    stock[name] -= amount

def comprar (name):
    #Comprueba stock
    try:
        x = int(input("\t-> Que cantidad?\n"))
        if x < 0:
            raise ValueError("ERROR. Cantidad negativa!")
        else:
            if x <= stock.get(name): #Comprueba valor correcto
                add_producto(name, x)
            else:
                if x > stock.get(name): 
                    print("\t-> Solo quedan " + str(stock.get(name)) + " " + name + "\n") #Posible reiteracion para volver a preguntar cantidad
    except ValueError as e:
        print(e) #Si se retornara el error podriamos saltarnos mediante un control en 'MAIN' la siguiente función que se ejecutaria 'finalizar()'

def mostrar_cesta(cesta_compra):
    total = 0 #Posible retrurn para funcion de pago

    #HEAD
    print("--------------------------------------------------------------------------------------")
    print("Producto \t\t Cantidad \t\t Precio \t\t Valor")
    print("--------------------------------------------------------------------------------------")

    #PRODUCTOS
    ''' OPCION _solo_key_: para recorrer con for!
    for k in lista_compra:
        if lista_compra.get(k) > 0 :
            print( k + " \t\t " + str(lista_compra.get(k)) + " \t\t " + str(precio.get(k)) + " \t\t Valor")
    '''
    for k, aux in cesta_compra.items():
        if aux > 0 :
            #calculo de valores
            coste = aux * precio.get(k)
            total += coste
            print( k + " \t\t\t " + str(aux) + " \t\t\t " + str(precio.get(k)) + " € \t\t\t " + str(coste) + " €" )
    
    #TOTAL - anteriormente calculado, calculo de valores^
    print("--------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t TOTAL \t\t\t" + str(total) + " €")

def mostrar_productos():
    for k, aux in precio.items():
        if stock[k] > 0: #hace que no aparezca en el listado pero si puedes volver a pedirla. ERROR. Faltaria una funcion si_esta_stock
            print(k + "\t" + str(aux) + " €")
    print('\n')

def finalizar_servicio():
    check = input("\t-> Desea seguir pidiendo Y/N? ")
    #Contorla que entre Y/y pero resto de entradas no
    if check.upper() == 'Y':
        mostrar_productos()
        return True
    else:
        return False


#-------------   
# --- MAIN ---
#-------------

print("\n\t-> Bienvenid@!\n") #Posible función de entrada/login

control = True #Control para while, NO EXISTE DO-WHILE EN PYTHON?!
mostrar_productos()

#Bucle de pedido
while control:
    pedido = input("\t-> Que desea?\n")
    #Control existencia de pedido
    try:
        if not pedido in set(precio.keys()): 
            raise ValueError("ERROR. Introduzca un producto valido.\n")
        else:
            #Si existe, se realiza el servicio
            comprar(pedido) 
            #Pregunta para finalizar servicio, controla salir del bucle infinito
            control = finalizar_servicio()
    except ValueError as e:
        print(e)

    

#Si acaba servicio, muestra la cuenta
mostrar_cesta(cesta)

print("\n\t-> Gracias!")#Posible funcion de pago