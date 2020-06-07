from random import sample

class Product:
    """ 
    Models acme products.

    Parameters
    -----------------------

    name : string
    price : int
    weight : int
    flammablilty : float
    identifier : int


    """

def  __init__(self, name, price=20, weight=20, flammablilty=0.5, identifier=None):
    self.name =  name       
    self.price = price
    self.weight = weight
    self.flammablilty = flammablilty
    self.identifier = identifier

def stealability():
    price = 10
    weight = 20
    result = price/weight
    if result < 0.5:
        print("Not so Stealable")
    elif result >= 0.5: 
        print("Kinda Stealable")
    else:
        print("Very Stealable")
    return 
def explode():
    flammablilty = 0.5
    weight = 20
    result1 = flammablilty * weight
    if result1 < 10:
        print("Fizzle")
    elif result1 >= 10 or result1 < 50:
        print("boom!")
    else:
        print("BABOOM")
    return 
class BoxingGlove(Product):
    def  __init__(self, name, price=20, weight=10, flammablilty=0.5, identifier=None):
        self.name =  name       
        self.price = price
        self.weight = weight
        self.flammablilty = flammablilty
        self.identifier = identifier
def explode():
        flammablilty = 0.5
        weight = 20
        result1 = flammablilty * weight
        if result1 < 10:
            print("Fizzle")
        elif result1 >= 10 or result1 < 50:
            print("boom!")
        else:
            print("BABOOM")
        return result1
def punch():
    weight = 10
    if weight < 5:
        print("That Tickles")
    elif weight >= 5 or weight < 50:
        print("Hey that Hurt")
    else:
        print("OUCH")    
    return
print(punch())
print(stealability())
print(explode())

       

          
    