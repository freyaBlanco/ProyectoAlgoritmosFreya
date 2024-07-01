import requests
import urllib.request
import json
from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido
from Product import Product
from Restaurant import Restaurant
from Cliente import Cliente

# Constructor de la clase App
class App():
    def __init__(self):
        # Listas vacias para almacenar los objetos
        self.Equipos= []
        self.Partidos = []
        self.Estadios = []
        self.Restaurants = []
        self.Productos = []
        self.Bebida = []
        self.Comida = []

# Método para ejecutar la aplicación
    def run(self):
        # Método para llamar a la API y almacenar los objetos en las listas
        self.api()
        # Método para llamar al menú
        self.menu()

# Método para obtener los datos de la API
    def api(self):

        # Se obtienen los datos de los equipos de la API
        URL = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
        response = requests.get(URL)
        response = response.json()
        
        for equipo in response:
           # Crea un objeto Equipo con los datos obtenidos
           nuevo = Equipo(equipo["id"], equipo["code"], equipo["name"], equipo["group"])
            # Agrega el objeto Equipo a la lista de equipos
           self.Equipos.append(nuevo)

        # Obtiene los datos de los estadios de la API
        URL = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
        response = requests.get(URL)
        response = response.json()

        for estadio in response:
            # Crea un objeto Estadio con los datos obtenidos
            nuevo = Estadio(estadio["id"], estadio["name"], estadio["city"], estadio["capacity"])
            
            # Obtiene los datos de los restaurantes del estadio
            listado_restaurante = []
            for restaurante in estadio["restaurants"]:
                # Crea un objeto Restaurantes con los datos obtenidos
                nuevo_restaurante = Restaurant(restaurante["name"])
                
                # Obtiene los datos de los productos del restaurante
                listado_productos = []
                for producto in restaurante["products"]:
                    nuevo_producto = Product(producto["name"], producto["quantity"], producto["price"], producto["stock"], producto["adicional"])
                    listado_productos.append(nuevo_producto)
                    self.Productos.append(nuevo_producto)
                # Crea un objeto Producto con los datos obtenidos
                nuevo_producto = Product(producto["name"], producto["quantity"], producto["price"], producto["stock"], producto["adicional"])
                # Agrega el objeto Producto a la lista de productos
                listado_productos.append(nuevo_producto)
                self.Productos.append(nuevo_producto)

            # Agrega el objeto Restaurant a la lista de restaurantes
                listado_restaurante.append(nuevo_restaurante)

            # Agrega el objeto Estadio a la lista de estadios
            self.Estadios.append(nuevo)

        # Obtiene los datos de los partidos de la API
        URL = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
        response = requests.get(URL)
        response = response.json()

        for partido in response:
            # Crea un objeto Partido con los datos obtenidos
            nuevo = Partido(partido["id"],partido ["number"], partido["home"], partido["away"], partido["date"], partido ["group"], partido["stadium_id"])
            # Asigna los objetos Equipo correspondientes a los equipos de casa y visitante
            for equipo in self.Equipos:
                if partido["home"]["id"] == equipo.id:
                    nuevo.home = equipo
            for equipo in self.Equipos:
                if partido["away"]["id"] == equipo.id:
                    nuevo.away = equipo
            # Asigna el objeto Estadio correspondiente al estadio del partido
            for estadio in self.Estadios:
                if partido["stadium_id"] == estadio.id:
                    nuevo.stadium_id = estadio

            # Agrega el objeto Partido a la lista de partidos
            self.Partidos.append(nuevo)

    def menu(self):

        # Llama al método api para obtener los datos de la API
        self.api()

        # Se muestra el menú principal
        while True:
            print(''' ---BIENVENIDO A LA EUROCOPA 2024--- 
        Menu:
            1. Mostrar Partidos por equipo
            2. Mostrar Partidos por estadio
            3. Mostrar partidos por fecha                     
            4. Mostrar productos por nombre
            5. Mostrar productos por tipo
            6. Mostrar productos por precio
            7. Venta de entradas
            8. Venta de restaurantes
            9. Cerrar sistema
            ''')

            seleccion = (input("\nIngrese el número de su elección: "))

            if seleccion == '1':
                print(' PARTIDOS POR EQUIPO ')
                equipo = input("¿Qué equipo quiere buscar? ").lower()
                for partido in self.Partidos:
                    if equipo in partido.home.pais.lower() or equipo in partido.away.pais.lower():
                        partido.show()
                
            
            elif seleccion == '2':
                print(' PARTIDOS POR ESTADIO ')
                estadio = input("¿Qué estadio quiere buscar? ").lower()
                for partido in self.Partidos:
                    if estadio in partido.stadium_id.name.lower():
                        partido.show()

            elif seleccion == '3':
                print(' PARTIDOS POR FECHA ')
                fecha = input("¿Qué fecha quiere buscar? ").lower()
                for partido in self.Partidos:
                    if fecha in partido.date.lower():
                        partido.show()

            elif seleccion == '4':
                print(' PRODUCTOS DISPONIBLES POR NOMBRE ')
                name = input("¿Nombre del producto que quiere buscar? ").lower()
                for producto in self.Productos:
                    if name in producto.name.lower():
                        producto.show()

            elif seleccion == '5':
                print(' PRODUCTOS DISPONIBLES POR TIPO ')
                tipo = input('''¿Qué tipo de producto quiere buscar? 
            1. Bebida
            2. Comida 
        ''').lower()
                for producto in self.Productos:
                    if tipo == '1' and (producto.adicional == "alcoholic" or producto.adicional ==  "non-alcoholic"):
                        producto.show()
                    elif tipo == '2' and (producto.adicional == "plate" or producto.adicional ==  "package"):
                        producto.show()

            elif seleccion == '6':
                print(' PRODUCTOS DISPONIBLES POR PRECIO ')
                precio = input("¿Qué precio quiere buscar? ").lower()
                for producto in self.Productos:
                    if precio in producto.price.lower():
                        producto.show()

            elif seleccion == '7':
                self.venta()

            elif seleccion == '8':
                self.venta_restaurante()

    def venta(self):
        print('VENTA DE ENTRADAS')
        print("Ingrese sus datos, partido y tipo de estrada que desee comprar")
        nombre = input("Nombre: ")
        cedula = input("Cedula: ")
        #self.venta_restaurante(cedula)
        edad = input("Edad: ")

        print("Acá tiene una lista de los partidos disponibles")
        for partido in self.Partidos:
            partido.show()

        selccion = input("Ingrese el nuemro del partido que desea comprar: ")
        for partido in self.Partidos:
            if int(selccion) == partido.number:
                partido.show()   
        
        capacidad = partido.stadium_id.capacity

        tipo_entrada = input('''Tipo de estrada que desea comprar: 
        1. General
        2. VIP
        ''')
        
        if tipo_entrada == '1':
            precio_base = 35
            print("ENTRADA GENERAL")
            capacidad = partido.stadium_id.capacity[0]
        
        elif tipo_entrada == '2':
            precio_base = 75
            print('''ENTRADA VIP
                  
            Prodra disfrutar de los productos del restaurante
            ''')
            capacidad = partido.stadium_id.capacity[1]
        
        else:
            print("Tipo de entrada no válido. Debes elegir General o VIP.")

        #Cantidad de filas segun su capacidad
        fila = 
        
        #Mapa del estadio, es una matriz
        asientos = []
        for i in range(1, (capacidad//10)+1):
            asientos_por_fila = []
            for j in range(1, 11):
                if len(str(i)) == 1:
                    i = "0"+str(i)
                asiento = f"{i}**{j}"
                asientos_por_fila.append(asiento)
            asientos.append(asientos_por_fila)
        
        print("Primero es la fila y luego la columna")

        fila = input("Ingresa la fila ")
        while not fila.isnumeric() or not int(fila) in range(1, row+1):
            fila = input("Ingresa la fila ")

        columna = input("Ingresa la columna ")
        while not columna.isnumeric() or not int(columna) in range(1, 11):
            columna = input("Ingresa la columna  ")
        
        asiento = f"{columna}**{columna}"
    

        #Verificar si la cedula es un numero vampiro 
        if sorted(cedula) == sorted(str(int(cedula) ** 2)):
            descuento = precio_base * 0.5
            print("¡Tienes un 50% de descuento por ser un número vampiro!")

        # Calcular impuesto (IVA)
        iva = precio_base * 0.16

        # Calcular costo total
        costo_total = precio_base + iva - descuento if "descuento" in locals() else precio_base + iva

        # Mostrar información al cliente
        print("INFORMACIÓN DE SU COMPRA")
        print(f"Asiento: {asiento}")
        print(f"Costo de la entrada ({tipo_entrada}): ${precio_base:.2f}")
        print(f"Subtotal: ${precio_base:.2f}")
        if "descuento" in locals():
            print(f"Descuento: ${descuento:.2f}")
        print(f"IVA (16%): ${iva:.2f}")
        print(f"Total a pagar: ${costo_total:.2f}")
        print("¡Gracias por su compra!")

    # Gestion de asistencia a partidos 
    def validar_boleto(self, codigo):
    
        #Valida la autenticidad del boleto con el código único del mismo
   
        # Busca el partido correspondiente al código de boleto
        for partido in self.Partidos:
            if partido.id == codigo:
            # Verifica si el boleto ya fue utilizado
                if partido.asistencia:
                    print("Boleto ya fue utilizado. No es válido.")
                return False
            else:
                # Marca la asistencia del partido como True
                partido.asistencia = True
                print("Boleto auténtico. Asistencia registrada.")
                return True
        print("Boleto no encontrado. No es válido.")
        return False
       

    #Gestion de restaurantes 
    def venta_restaurante(self, cedula):
        print("\nVENTA DE RESTAURANTES\n")
        print("Para ingresar en la venta de restaurantes, debemos chequear si usted es un cliente VIP: \n\n")
        while True:
            try:
                cedula = int(input("\nIngrese su cédula:  "))
                if cedula <= self.venta(cedula):
                    raise Exception
                break
            except:
                print("Cédula inválida. ")

        if not self.is_vip_client(cedula):
            print("Lo sentimos, no eres un cliente VIP.")
            return

        print("Productos disponibles:")
        self.show_products()

        productos_seleccionados = []
        while True:
            try:
                seleccion = int(input("\nIngrese el ID del producto que desea comprar o 0 para terminar: "))
                if seleccion == 0:
                    break
                producto = self.get_product_by_id(seleccion)
                if producto:
                    productos_seleccionados.append(producto)
                else:
                    print("Producto no encontrado.")
            except:
                print("Error al seleccionar producto.")

        if not productos_seleccionados:
            print("No ha seleccionado ningún producto.")
            return

        subtotal = 0
        for producto in productos_seleccionados:
            subtotal += producto.price

        iva = subtotal * 0.16
        total = subtotal + iva

        if self.is_perfect_number(cedula):
            descuento = total * 0.15
            total -= descuento

        print("Resumen de su compra:")
        print("Productos:")
        for producto in productos_seleccionados:
            print(f"  - {producto.name} (${producto.price:.2f})")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"IVA (16%): ${iva:.2f}")
        if self.is_perfect_number(cedula):
            print(f"Descuento (15%): ${descuento:.2f}")
        print(f"Total: ${total:.2f}")

        while True:
            respuesta = input("¿Desea proceder con la compra? (s/n): ")
            if respuesta.lower() == 's':
                self.restaurante.vender_productos(productos_seleccionados)
                print("Pago exitoso. ¡Gracias por su compra!")
                return
            elif respuesta.lower() == 'n':
                print("Compra cancelada.")
                return
            else:
                print("Respuesta inválida. Intente nuevamente.")

    def is_vip_client(self, cedula):
        # Verificar si el cliente es VIP (ya compró una entrada VIP)
        # ...
        pass

    def is_perfect_number(self, cedula):
        # Verificar si la cédula es un número perfecto
        # ...
        pass

    def get_product_by_id(self, id):
        # Buscar producto por ID
        for producto in self.Productos:
            if producto.id == id:
                return producto
        return None

    def show_products(self):
        # Mostrar productos disponibles
        for producto in self.Productos:
            print(f"ID: {producto.id}, Nombre: {producto.name}, Precio: ${producto.price:.2f}")
    




                    
                        
                    

            

                

    




#Crea una funcion menu (metodo de app) que se llame en la funcion run, en ella vas a mostrar las oppciones del programa esto los sacaras del docuemnto, junto al menun has su verificacion su su estructura if-else para ser usada mas adelante, crea una funcion para opcion del menu y ponle ´pass dentro para que no te de error