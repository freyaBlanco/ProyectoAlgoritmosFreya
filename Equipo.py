class Equipo():
    def __init__(self, id, codeFIFA, pais, group):
        self.id = id
        self.codeFIFA = codeFIFA
        self.pais = pais
        self.group = group

    def show(self):
        print (f'''
ID: {self.id}
CODEFIFA: {self.codeFIFA}
PAIS: {self.pais}
GROUP: {self.group}
''')
