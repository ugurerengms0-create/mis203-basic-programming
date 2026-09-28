#taking variables
item1_name = input("First item:")
item1_qty = int(input("First quantity:"))
item1_price = float(input("First item price:"))

item2_name = input("Second item:")
item2_qty = int(input("Second quantity:"))
item2_price = float(input("Second item price:"))

dlv = float(input("Delivery price:"))
tax_prg = float(input("Tax percentage:"))
#sub
item1_total = item1_qty * item1_price
item2_total = item2_qty * item2_price
subtotal = item1_total + item2_total
#tax and final total calculation
tax_amount = subtotal * (tax_prg / 100)
final_total  = subtotal + tax_amount + dlv
#printing
print("\n----Calculation----")
print(f"{item1_qty} x {item1_name} - Price: {item1_price:.2f} TRY - Total: {item1_total:.2f} TRY")
print(f"{item2_qty} x {item2_name} - Price: {item2_price:.2f} TRY - Total: {item2_total:.2f} TRY")
print(f"Subtotal: {subtotal:.2f} TRY")
print(f"Tax: (%{int(tax_prg)}): {tax_amount:.2f} TRY")
print(f"Delivery Fee: {dlv:.2f}TRY")
print(f"Final total: {final_total:.2f} TRY")
