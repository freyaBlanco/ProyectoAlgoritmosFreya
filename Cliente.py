class Cliente:
    def __init__(self, nombre, cedula, edad, partido, tipo_entrada):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.partido = partido
        self.tipo_entrada = tipo_entrada

    def show(self):
        print(f'''
NOMBRE: {self.nombre}
CEDULA: {self.cedula}
EDAD: {self.edad}
PARTIDO: {self.partido}
TIPO ENTRADA: {self.tipo_entrada}
''')


        