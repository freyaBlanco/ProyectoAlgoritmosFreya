class Product():
    def __init__(self, name, quantity, price, stock, adicional):
        self.name = name 
        self.quantity = quantity
        self.price = price
        self.stock = stock 
        self.adicional = adicional
        if self.adicional == "alcoholic" or self.adicional == "non-alcoholic":
            self.tipo_producto = "Bebida"
        else:
            self.tipo_producto = "Comida"


    def show(self):
        print(f'''
NAME: {self.name}
QUANTITY: {self.quantity}
PRICE: {self.price}
STOCK: {self.stock}
TIPO_PRODUCTO: {self.tipo_producto}
FORMATO: {self.adicional}
''')
    