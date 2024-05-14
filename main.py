class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat_meal(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print('каррр')
    def eat_meal(self):
        print('ест сыр')
class Goat(Animal):
    def make_sound(self):
        print('меее')
    def eat_meal(self):
        print('ест траву')
class Frog(Animal):
    def make_sound(self):
        print('ква')
    def eat_meal(self):
        print('ест комаров')
class Zoo(Animal):
    def __init__(self, name, age):
        self.animal = Animal # Композиция

    def add_animal(self, animal_list, name):  # функция добавления животного
        animal_list.append(name)
        print(f'животное добавлено')

    def remove_animal(self, animal_list, name):  # Удаление животного
        animal_list.remove(name)

class  Veterinarian(Animal):
    def __init__(self, name):
        self.animal = Animal # Композиция
    def treatment_animal(self):
         print('ветеринар лечит животного')

def make_sound(object): # функция издания звука
    print(объект.make_sound())

def eat_meal(object): # функция что ест
    print(object. eat_meal())

list_object = [Bird('имя', 'возраст'), Goat('имя','возраст'), Frog('имя','возраст')]
for object in list_object:
    object.make_sound()

for object in list_object:
    object.eat_meal()


animals = []
animal1 = Zoo('слон', 5)
animal2 = Zoo('черепаха', 120)

animal1.add_animal(animals, 'корова')

animal3 = Veterinarian('слон')
animal3.treatment_animal()
