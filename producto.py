#CLASE OPINIONES, el producto albergara una lista de opiniones
class Opiniones:
    #__INIT__
    def __init__(self, nombre, valor, text):
        self.__nombre = nombre
        self.__valor = valor
        self.__text = text
    
    #Getters
    def get_nombre(self):
        return self.__nombre
    def get_valor(self):
        return self.__valor
    def get_text(self):
        return self.__text

#CLASE PRODUCTO
class Producto:

    cantidad = 0

    def __init__(self, nombre, precio = 0.0, stock = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.op_list = []
        Producto.cantidad += 1

    def get_producto(self):
        return self.__nombre , self.__precio , self.__stock

    def get_nombre(self):
        return self.__nombre

    def get_stock(self):
        return self.__stock

    def get_precio(self):
        return self.__precio

    def set_producto(self, nombre, precio = 0.0, stock = 0):
        self.__nombre = nombre
        if precio != 0.0:
            self.__precio = precio
        if stock != 0:
            self.__stock = stock

    def set_stock(self, stock):
        self.__stock = stock

    def set_precio(self, precio):
        self.__precio = precio

    #OPINIONES
    def add_opinion(self, nombre, valor, text):
        op = Opiniones(nombre, valor, text)

        self.op_list.append(op)
    
    def get_opinion(self):
        for i in range(0,len(self.op_list)):
            print(f"{self.op_list[i].get_nombre()} {self.op_list[i].get_valor()}/10\n{self.op_list[i].get_text()}\n")


#Prueba funcionan getters and setters producto
'''b = Producto("stout", 5, 10)

b.get_producto()
print('\n')

b.set_precio(5.5)


b.set_stock(5)


b.get_producto()
print('\n')

b.set_producto("ale")


b.get_producto()
print('\n')

b.get_precio()
print('\n')

b.get_stock()
print('\n')'''

#Prueba funcionan opiniones
'''b = Producto("stout", 5, 10)
b.add_opinion("Jesus", 8.7, "Me ha encantado.")
b.add_opinion("Manuel", 6.3, "No es lo que esperaba, pero funciona.")
b.get_opinion()'''