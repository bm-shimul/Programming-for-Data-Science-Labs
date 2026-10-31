
products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]


def apply_discount(total):
    if total >= 2000:
        discount = total * 0.10
        return total - discount
    else:
        return total


total = 0

for product in products:
    cost = product["price"] * product["quantity"]
    total += cost

    print(product["name"], "=", cost)


final_total = apply_discount(total)

print("\nTotal Cost:", total)
print("Final Cost after Discount:", final_total)
