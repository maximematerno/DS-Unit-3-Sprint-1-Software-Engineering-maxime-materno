import random


class Product():

    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        price = self.price
        weight = self.weight

        price_to_weight_ratio = float(price / weight)

        if price_to_weight_ratio < 0.5:
            return print("Not so stealable")
        elif (price_to_weight_ratio >= 0.5) and (price_to_weight_ratio < 1.0):
            return print("Kinda stealable.")
        else:
            return print("Very stealable!")

    def explode(self):
        flammability = self.flammability
        weight = self.weight

        flam_to_weight = float(flammability * weight)

        if flam_to_weight < 10:
            return print("...fizzle.")
        elif (flam_to_weight >= 10) and (flam_to_weight < 50):
            return print("...boom!")
        else:
            return print("...BABOOM!!")


class BoxingGlove(Product):
    def __init__(self, name):
        Product.__init__(self, name)
        self.weight = 10

    def explode(self):
        return print("...it's a glove.")

    def punch(self):
        weight = self.weight

        if weight < 5:
            return print("That tickles.")
        elif (weight >= 5) and (weight < 15):
            return print("Hey that hurt!")
        else:
            return print("OUCH!")
