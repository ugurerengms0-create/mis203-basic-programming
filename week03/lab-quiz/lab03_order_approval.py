print("=== Order Approval System ===")

order_amount = float(input("Enter unit price (TRY): "))
requested_quantity = int(input("Enter requested quantity: "))
available_stock = int(input("Enter available stock: "))

member_input = input("Is the customer a member? (y/n): ").strip().lower()
if member_input == "y":
    is_member = True
else:
    is_member = False

if requested_quantity <= 0:
    print("Order Rejected: Invalid requested quantity!")
elif requested_quantity > available_stock:
    print("Order Rejected: Insufficient stock!")
else:
    total_price = order_amount * requested_quantity

    if is_member and total_price >= 500:
        discount = total_price * 0.10
        approval_reason = "Approved with 10% member discount."
    else:
        discount = 0.0
        approval_reason = "Approved standard order (No discount)."

    final_price = total_price - discount

    print("--- Order Approved ---")
    print("Approval Reason:", approval_reason)
    print(f"Discount: {discount:.2f} TRY")
    print(f"Original Amount: {order_amount:.2f} TRY")
    print(f"Final Price: {final_price:.2f} TRY")
