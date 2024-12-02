class Animal:

        def __init__(self,name):
            self.name = name

        def eat(self):
            print(f'{self.name} can eat')
        def drink(self):
            print(f'{self.name} can drink')



class Cat(Animal):

    def cute(self):
        print(f'{self.name} is so cute')


class Ragdoll(Cat):

    def __init__(self,name,color):
        super().__init__(name)
        self.color = color

    def __str__(self):
        return f'{self.name} is with {self.color}'


Me = Animal('Me')
Me.eat()
Uriel = Ragdoll('Uriel','white')
print(Uriel)