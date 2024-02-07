num_coffees = int(input("Enter the number of coffees: "))
num_muffins = int(input("Enter the number of muffins: "))


coffee_price = 5
muffin_price = 4


subtotal = (num_coffees * coffee_price) + (num_muffins * muffin_price)


tax_rate = 0.06
tax_amount = subtotal * tax_rate


total = subtotal + tax_amount

print("=== Receipt ===")
print(f"Number of coffees: {num_coffees}")
print(f"Number of muffins: {num_muffins}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (6%): ${tax_amount:.2f}")
print(f"Total: ${total:.2f}")
