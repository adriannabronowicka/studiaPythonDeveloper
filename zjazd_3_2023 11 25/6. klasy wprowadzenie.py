
class Crocodile:
    tails = True
    limbs = 4
    wiki_Link = ""

    # dunder method (double underscore method)
    def __init__(self, name, place_of_habitat):
        self.name = name
        self.place = place_of_habitat

    def method(self):
        pass

    def eat(self):
        pass

    @staticmethod
    def get_population_count():
        # internet .get(....)
        return 99245

    @classmethod
    def get_population_limbs_count(cls):
        crocodile_count = cls.get.population_count()
        return crocodile_count * cls.limbs


def function():
    pass


integer_szczepan = int(99)
andrzej = Crocodile("Andrzej", "Zoo in Wroclaw")
blazej = Crocodile("Blazej", "Amazon forest")

print("ok")