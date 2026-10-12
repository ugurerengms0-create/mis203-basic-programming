# 1. Girdiler ve Kontroller
starting = float(input("Starting balance: "))
while starting < 0:
    starting = float(input("Starting balance cannot be negative. Try again: "))

deposit = float(input("Monthly deposit: "))
while deposit <= 0:
    deposit = float(input("Monthly deposit must be positive. Try again: "))

rate = float(input("Monthly interest rate (%): "))
while rate < 0:
    rate = float(input("Monthly interest rate cannot be negative. Try again: "))

goal = float(input("Savings goal: "))
while goal <= 0:
    goal = float(input("Savings goal must be positive. Try again: "))

balance = starting
total_interest = 0.0

# 2. Başlangıç zaten hedefi tutturduysa
if balance >= goal:
    print("\nStarting balance already meets the goal!")
    print("Goal reached in 0 months.")
    print(f"Final balance: {balance:.2f}")
    print(f"Total interest earned: {total_interest:.2f}")
else:
    # 3. Tablo Başlığı
    print(f"\n{'Month':<8}{'Interest':<15}{'Balance'}")
    print("-" * 35)

    # 4. Ay Ay Döngü 
    month = 0
    while month < 60:
        month += 1
        interest = balance * rate / 100
        total_interest += interest
        balance += interest + deposit

        print(f"{month:<8}{interest:<15.2f}{balance:.2f}")

        if balance >= goal:
            break

    # 5. Sonuç Özeti
    print("\n--- Summary ---")
    if balance >= goal:
        print(f"Goal reached in {month} months.")
    else:
        print("Goal not reached after 60 months.")

    print(f"Final balance: {balance:.2f}")
    print(f"Total interest earned: {total_interest:.2f}")