num_coffees = int(input("Enter the number of coffees: "))
num_muffins = int(input("Enter the number of muffins: "))
num_bread = int(input(" Enter the amount of Breads: "))
num_chocolate = int(input(" Enter the amount of chocolates: "))

coffee_price = 5
muffin_price = 4
bread_price = 2
chocolate_price = 3


subtotal = (num_coffees * coffee_price) + (num_muffins * muffin_price)+(num_bread * bread_price) + (num_chocolate * chocolate_price)


tax_rate = 0.06
tax_amount = subtotal * tax_rate


total = subtotal + tax_amount

print("=== Receipt ===")
print(f"Number of coffees: {num_coffees}")
print(f"Number of muffins: {num_muffins}")
print(f"Number of Breads: {num_bread}")
print(f"Number of Chocolates: {num_chocolate}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (6%): ${tax_amount:.2f}")
print(f"Total: ${total:.2f}")
