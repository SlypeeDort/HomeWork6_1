class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name
        print(f'{name}, Живой: {self.alive}, Сытый: {self.fed}')

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        if not food.edible:
            print(f'{self.name} не стал есть {food.name}')
            self.fed = False
            self.alive = False


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name
        print(f'{name}, Cъедобный: {self.edible}')


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


a1 = Predator('Волк с Уолл-Стрит')
p1 = Flower('Цветик семицветик')
a1.eat(p1)
print(f'Живой {a1.alive}')
print(f'Сытый: {a1.fed}\n')
a2 = Mammal('Хатико')
p2 = Fruit('Заводной апельсин')
a2.eat(p2)
print(f'Живой: {a2.alive}')
print(f'Сытый: {a2.fed}')
