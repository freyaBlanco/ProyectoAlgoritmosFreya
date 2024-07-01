class Estadio ():
    def __init__(self, id, name, city, capacity):
        self.id = id
        self.name = name 
        self.city = city
        self.capacity = capacity
        self.restaurants = []

    def show(self):
        print(f'''
ID: {self.id}
NAME: {self.name}
CITY: {self.city}
CAPACITY: {self.capacity}
''')