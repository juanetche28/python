import datetime as datetime


class Customer:
    def __init__(self, name, lastName, idFiscal, age):
        """ Inicializo los atributos de nombre, apellido, edad y DNI """
        self.name = name
        self.lastName = lastName
        self.idFiscal = idFiscal  # DNI, Dato unico e irrepetible
        self.age = age
        self.purchases = 0 # Voy a usar un contador de cant. de compras
    
    def __str__(self):
        text = "Customer: "+self.name+" "+self.lastName
        return text

    def receipt(self, idProduct, price, quantity):
        """ Voy a simular un recibo de venta """
        self.idProduct = idProduct
        self.price = price
        self.quantity = quantity
        current_date = datetime.date.today()
        subtotal = price * quantity
        iva = subtotal * 0.21
        total = subtotal + iva
        self.purchases += 1 # Sumo esta compra al contador.
        print(self.name+", Gracias por su compra! \n ---Recibo--- \n"+"Fecha: "+str(current_date)+"\n"+"Producto: "+str(self.idProduct)+"\n"+"Subtotal: "+str(subtotal)+"\n"+"Iva: "+str(iva)+"\n"+"Total: "+str(total))

    def readPurchases(self):
        """Voy a leer la cantidad de compras del cliente"""
        print("Cliente: "+self.name+" "+self.lastName+"\nCant de compras: "+str(self.purchases))

    def addPurchases(self, purchases):
        """Incremento la cant de compras"""
        self.purchases += purchases

    def updatePurchase(self, purchases):
        """Actualizo la cant de compras por el importe que quiero"""
        self.purchases = purchases

"""Creo un Cliente, Juan Cruz"""
customerExample = Customer("Juan Cruz", "Etcheverry", 1111, 30)
print(customerExample) # No da error de object porque uso __str__

"""Creo un recibo de venta para Juan Cruz"""
receipt = customerExample.receipt("fernet", 3000, 4)

customerExample.readPurchases() #Muestro la Cant de compras

"""Voy a incrementar la cantidad de compras"""
customerExample.addPurchases(3)
customerExample.readPurchases() #Muestro la Cant de compras

"""Voy a actualizar la cantidad de compras"""
customerExample.updatePurchase(2)
customerExample.readPurchases() #Muestro la Cant de compras


