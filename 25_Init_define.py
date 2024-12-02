class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(f'dog {self.name},age{self.age} bark....')
    def __str__(self):
        return f'name: {self.name},age:{self.age}'


my_dog = Dog("Tom",7)
my_dog.bark()
print(my_dog)


`

