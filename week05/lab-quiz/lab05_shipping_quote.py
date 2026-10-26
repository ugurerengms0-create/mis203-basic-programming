# Explanation for Question 4: Difference between print and return
# - return: Returns the result of the function back to where it was called. This value can be assigned
#   to a variable and used in further operations.
# - print: Simply outputs to the console (screen). You cannot use the value elsewhere in the program (its value becomes None).
def calculate_subtotal(price, quantity):
    return price * quantity


def calculate_discount_rate(subtotal):
    if subtotal >= 500:
        return 0.10
    return 0.0


def calculate_shipping_fee(subtotal):
    if subtotal >= 300:
        return 0.0
    return 49.99


def calculate_final_total(subtotal, discount_rate, shipping_fee):
    """Calculates the final total considering subtotal, discount, and shipping fee."""
    discount_amount = subtotal * discount_rate
    final = (subtotal - discount_amount) + shipping_fee
    return round(final, 2)


# --- Assert Checks (Acceptance Check 3) ---
# 1. Threshold Boundary Test (Discount check at exactly 500 TL subtotal)
assert calculate_discount_rate(500) == 0.10, "Test Failed: 500 TL should have a 10% discount."

# 2. Shipping Threshold Boundary Test (Shipping fee should apply below 300 TL)
assert calculate_shipping_fee(250) == 49.99, "Test Failed: Shipping should be 49.99 for 250 TL."

# 3. Final Total Test
assert calculate_final_total(100, 0.0, 49.99) == 149.99, "Test Failed: Incorrect calculation."

print("All assert tests passed successfully!")


# --- Sample Orders (Acceptance Checks 1 and 2: No code duplication, functions are reused) ---
def process_order(order_no, price, quantity):
    print(f"\n--- Order #{order_no} ---")
    subtotal = calculate_subtotal(price, quantity)
    discount_rate = calculate_discount_rate(subtotal)
    shipping_fee = calculate_shipping_fee(subtotal)
    final_total = calculate_final_total(subtotal, discount_rate, shipping_fee)

    print(f"Subtotal: {subtotal} TL")
    print(f"Discount Rate: %{int(discount_rate * 100)}")
    print(f"Shipping Fee: {shipping_fee} TL")
    print(f"Final Total: {final_total} TL")


# Running at least two sample orders (Reusing the same functions without code duplication)
process_order(1, 150, 4)
process_order(2, 80, 2)
process_order(3, 200, 3)

