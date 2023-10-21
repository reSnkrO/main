import random
print("Hello Евгений Валерьевич")

class Student:

    def __init__(self,name):
        self.name = name
        self.money = 100
        self.rest = 0
        self.marks = 100
    def show_info(self):
        print("Name:",self.name)
        print("Money:",self.money)
        print("Rest:",self.rest)
        print("Marks:",self.marks)

    def set_name(self, new_name):
        self.name = new_name

    def set_work(self, amount):
        self.money += amount

    def set_study(self, amount):
        self.marks += amount

    def get_name(self):
        return self.name

    def add_days(self,amount):
        self.rest += amount

    def spend(self,amount):
        self.money -= amount

    def is_alive(self):
        return self.money > 0


new_player=Student("Dan")



while new_player.is_alive():
    if new_player.money < 20:
        num = random.randint(0, 1)
        new_player.set_work(random.randint(1, 10))
    if new_player.money > 21:
        new_player.set_study(random.randint(1, 20))

    num = random.randint(1,2)

    if num == 1:
        new_player.add_days(random.randint(1,10))
    elif num == 2:
        new_player.spend(random.randint(1,10))

new_player.show_info()