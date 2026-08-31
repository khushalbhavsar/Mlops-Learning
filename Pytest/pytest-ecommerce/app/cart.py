def add_to_cart(cart, product, quantity):
    if product["stock"] < quantity:
        return False

    cart.append(
        {
            "product_id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity,
        }
    )
    return True


def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total
