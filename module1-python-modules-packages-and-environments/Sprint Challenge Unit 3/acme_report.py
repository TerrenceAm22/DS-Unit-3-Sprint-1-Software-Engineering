import random

from random import sample, randint, choice
from acme import Product



ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

print(sample(ADJECTIVES, 3))

class report():
    def __init__(self, name, price=20, weight=20, flammablilty=0.5, identifier=random.randint(0, 1000)):
        self.name = name       
        self.price = price
        self.weight = weight
        self.flammablilty = flammablilty
        self.identifier = identifier
        
    def generate_products(num_products=30):
        products = []
        products = random.sample(range(0, 1000),30)
        return products
        
    def inventory_report(products):
        price = 20
        weight = 20
        flammablilty = 0.5
        average = sum(price) / len(price)
        products = set(products)
        print("Unique Product Names", len(products))
        print("Average Price", average)
        return
        
    
        
       
    


    if __name__ == '__main__':
        inventory_report(generate_products())
        


        





