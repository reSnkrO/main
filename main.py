import random
print("BLEAT'!!!")

class Player:

    def __init__(self,name):
        self.name = name
        self.HP = 100
        self.score = 0

    def show_info(self):
        print(self.name)
        print(self.HP)
        print(self.score)

    def set_name(self, new_name):
        self.name = new_name

    def set_heal(self, amount):
        self.HP += amount

    def get_name(self):
        return self.name

    def add_score(self,amount):
        self.score += amount

    def damage(self,amount):
        self.HP -= amount

    def is_alive(self):
        return self.HP > 0


new_player=Player("Dan")



while new_player.is_alive():
    if new_player.HP < 20:
        num = random.randint(0, 1)
        new_player.set_heal(random.randint(1, 50))

    num = random.randint(1,2)

    if num == 1:
        new_player.add_score(random.randint(1,10))
    elif num == 2:
        new_player.damage(random.randint(1,10))

new_player.show_info()