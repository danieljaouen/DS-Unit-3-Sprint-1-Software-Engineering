import random

from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num=30):
    return [
        Product(
            random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS),
            random.randint(5, 100),
            random.randint(5, 100),
            random.uniform(0.0, 2.5)
        )
        for _ in range(num)
    ]


def inventory_report(products):
    num_products = len(products)

    for product in products:
        print('---------------')
        print(
            f'Name: {product.name}, '
            f'Price: {product.price}, '
            f'Weight: {product.weight}, '
            f'Flammability: {product.flammability}, '
            f'Identifier: {product.identifier}'
        )

    print('---------------')
    print(
        f'Unique names: {len(set([product.name for product in products]))}, '
        f'Average price: {sum([product.price for product in products]) / num_products}, '
        f'Average weight: {sum([product.weight for product in products]) / num_products}, '
        f'Average flammability: {sum([product.flammability for product in products]) / num_products}'
    )


if __name__ == '__main__':
    inventory_report(generate_products())
