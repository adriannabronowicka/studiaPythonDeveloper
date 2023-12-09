class Human:

    def sleep(self):

    def eat(self):

    def drink(self):


class Bills:
    def calculate(self):

class Bobbuilder(Human):

    def __init__(self):
        self.bills = Bills()
    def build(self):

    def talk_to_car(self):

class UltraZarlok(Human):
    def eat(self):
        super().eat()
        super().eat()
        super().eat()

my_bob = Bobbuilder()

"""Encapsulation over inheritance"""
my_bob.bills.calculate()

