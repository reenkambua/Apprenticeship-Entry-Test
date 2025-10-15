def total_revenue(data):
    total = 0
    for item in data:
        total += item["price"] * item["quantity"]
    return total

sales = [
    {"item": "Pen", "price": 20, "quantity": 3},
    {"item": "Book", "price": 200, "quantity": 2},
    {"item": "Bag", "price": 800, "quantity": 1}
]

print("Total Revenue:", total_revenue(sales))  
