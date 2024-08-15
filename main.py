
class Cat():

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+ 'Is now sitting')

    def roll(self):
        print(self.name.title()+ 'Is now rolled over')

my_cat = Cat("Rajscleide", 10)
print(my_cat.name)
print(my_cat.age)

