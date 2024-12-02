import random
class Game:

    highest_score = 0
    name_highest_score = ""

    def __init__(self,name):
        self.name = name
        self.score = 0

    def play(self):
        self.score = random.randint(0,100)
        if self.score > Game.highest_score:
            Game.highest_score = self.score
            Game.name_highest_score = self.name
        with open('./data.txt', 'a', encoding='utf-8') as f:
            f.write(str(Game.highest_score)+'\n')
        with open('data.txt', 'r', encoding='utf-8') as f:
            while True:
                result = f.readline()
                if result == "":
                    break
                print(result, end='')


    def __str__(self):
        return (f'{self.name} get the {self.score}. '''
                f'{Game.name_highest_score} got the higest score {Game.highest_score}')


my_Game = Game('lan')
my_Game.play()
print(my_Game)

my_Game = Game('yuhan')
my_Game.play()
print(my_Game)

my_Game = Game('yuxuan')
my_Game.play()
print(my_Game)



