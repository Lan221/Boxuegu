class TV:

    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def movie(self,movie_name):
        self.name = movie_name

    def __str__(self):
        return f'TV {self.brand} price {self.price} euros play {self.name}'

my_tv = TV('LG',400)
my_tv.movie('dragon fly')

print(my_tv)

