class Restaurant():
    def __init__(self, name):
        self.name = name 
        self.productos = []

    def show(self):
        print(f'''
NAME: {self.name}
''')