def create_order(cart):
    if not cart:
        return None

    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]

    return {
        "status": "confirmed",
        "items": cart,
        "total": total,
    }
