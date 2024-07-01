from Estadio import Estadio
from Partido import Partido

class Busqueda: 

    def __init__(self, partidos, estadios, clientes):
        self.partidos = partidos
        self.estadios = estadios
        self.clientes = clientes
        pass

    def buscar_por_pais(self): 

        while True: 
            try: 
                pais = str(input("\n\nNombre de País:     "))

                if not "".join(pais.split()).isalpha():
                    raise Exception 

                break 

            except: 
                print("\nIntente de nuevo.\n")

        pais = pais.title()

        found = []

        for partido in self.partidos:

            if pais in partido.get_pais(partido): 
                found.append(partido)

        self.print_found(found)


    def Buscar_por_estadio(self): 
        for estadio in self.estadios: 
            Estadio.print_estadio(estadio)

        while True: 
            try: 
                seleccion = int(input("ID del estadio a buscar:     "))

                if seleccion not in range(1, 9): 
                    raise Exception

                break 

            except: 
                print("\nError. ID de estadio inválido.\n")


        selected_obj = self.estadios[seleccion-1]

        found = []

        for partido in self.partidos:
            if selected_obj == Partido.get_estadio(partido):
                found.append(partido)

        self.print_found(found)


    def Buscar_por_fecha(self): 
        print("\nBuscando por fecha:\n")

        while True: 
            try: 
                dia = input("Día a buscar: ")
                mes = input("Mes a buscar (número): ")
           
                if int(dia) in range(1,32) and int(mes) in range(1,13):
                    break

            except: 
                print("\n La información específicada no es correcta. \n")


        fecha = mes + "/" + dia + "/2024"

        found = []
        for partido in self.partidos: 
            if fecha in Partido.get_fecha(partido):
                found.append(partido)

        self.print_found(found)
        

    def print_found(self, found): 
        print("RESULTADOS DE BÚSQUEDA")
        for p in found: 
            Partido.print_partido(p)