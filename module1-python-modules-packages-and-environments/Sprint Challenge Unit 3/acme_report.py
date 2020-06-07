from random import randint, sample, uniform
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

print(sample(ADJECTIVES, 3))


def generate_products(num_products=30):
    products = ['boxing gloves', 'lint', 'shoes', 'bikes', 'cement']
    return products

def inventory_report(products):
    for i in products:
        print(i)
        return


if __name__ == '__main__':
    inventory_report(generate_products())



