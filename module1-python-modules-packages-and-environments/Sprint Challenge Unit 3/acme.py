import random

class Product():
    def  __init__(self, name, price=20, weight=20, flammablilty=0.5, identifier=random.randint(0, 1000)):
        self.name =  name       
        self.price = price
        self.weight = weight
        self.flammablilty = flammablilty
        self.identifier = identifier

    def stealability(self):
        self.price = 10
        self.weight = 20
        result = self.price/self.weight
        if result < 0.5:
            print("Not so Stealable")
        elif result >= 0.5: 
            print("Kinda Stealable")
        else:
            print("Very Stealable")
        return 
    def explode(self):
        self.flammablilty = 0.5
        self.weight = 20
        result1 = self.flammablilty * self.weight
        if result1 < 10:
            print("Fizzle")
        elif result1 >= 10 or result1 < 50:
            print("boom!")
        else:
            print("BABOOM")
        return 
class BoxingGlove(Product):
    def  __init__(self, name, price=20, weight=10, flammablilty=0.5, identifier=random.randint(0, 1000)):
        self.name =  name       
        self.price = price
        self.weight = weight
        self.flammablilty = flammablilty
        self.identifier = identifier
    def explode(self):
        print("its a glove")
        return 
        
    def punch(self):
        self.weight = 10
        if self.weight < 5:
            print("That Tickles")
        elif self.weight >= 5 or weight < 50:
            print("Hey that Hurt")
        else:
            print("OUCH")
            return

       


          
    