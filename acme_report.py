from random_word import RandomWords
import random
from statistics import mean


def generate_products():
    """ generate a given number of products (default 30),
    randomly, and return them as a list """
    # initialize list of noun and adj
    num_products = 30
    products = [0] * num_products
    prices = [0] * num_products
    weights = [0] * num_products
    flammabilities = [0] * num_products

    # initlize random word object
    random = RandomWords()

    adj = [random.get_random_word(includePartOfSpeech="adjective")
           for product in products]
    noun = [random.get_random_word(includePartOfSpeech="noun")
            for product in products]
    products = [noun + " " + adj for noun, adj in zip(adj, noun)]

    prices = [random.randint(5, 100) for price in prices]
    weights = [random.randint(5, 100) for weight in weights]
    flammabilities = [random.randint(0.0, 2.5)
                      for flammability in flammabilities]

    return products, prices, weights, flammabilities


def inventory_report(products, prices, weights, flammabilities):
    """ takes a list of products, and prints a "nice" summary """
    num_product = len(products)
    avg_price = mean(prices)
    avg_weight = mean(weights)
    avg_flam = mean(flammabilities)

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names: {}".format(num_product))
    print("Average price: {}".format(avg_price))
    print("Average weight: {}".format(avg_weight))
    print("Average flammability: {}".format(avg_flam))


if __name__ == '__main__':
    products, prices, weights, flammabilities = generate_products()
    inventory_report(products, prices, weights, flammabilities)
