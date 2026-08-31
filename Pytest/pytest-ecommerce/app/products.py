products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 50000,
        "stock": 10,
    },
    {
        "id": 2,
        "name": "Mobile",
        "price": 20000,
        "stock": 20,
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 2000,
        "stock": 50,
    },
]


def get_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def get_all_products():
    return products


def is_available(product_id, quantity):
    product = get_product(product_id)

    if product is None:
        return False

    return product["stock"] >= quantity
