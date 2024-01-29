def calculate_total(items):
    total = 0
    for item in items:
        total += item[1] * item[2]
    return total

def apply_discount(total, threshold, discount_rate):
    if total > threshold:
        discount = discount_rate
        total = total * (1 - discount)
    return total

# (item_name, price_per_item, quantity)
items = [('apple', 0.5, 15), 
         ('banana', 0.25, 2), 
         ('grape', 0.75, 3)]  

total = calculate_total(items)
total_with_discount = apply_discount(total, 10, 0.1)

print("Total after possible discount: ", total_with_discount)
