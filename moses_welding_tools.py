def welding_calculator_v2():
    print("\n=== Moses Welding Calculator V2 ===")

    try:
        price = float(input("Enter price per unit (₦): "))
        quantity = float(input("Enter quantity needed: "))
        profit_percentage = float(input("Enter desired profit percentage (%): "))
    except ValueError:
        print("\nInvalid input. Please enter numbers only.")
        input("Press Enter to return to menu...")
        return

    total = price * quantity
    profit = total * (profit_percentage / 100)
    final_price = total + profit

    print("\n--- Calculation Summary ---")
    print(f"Base total: ₦{total:,.2f}")
    print(f"Profit ({profit_percentage}%): ₦{profit:,.2f}")
    print(f"Final price to charge: ₦{final_price:,.2f}")

    input("\nPress Enter to return to menu...")
def basic_calculator():
    print("\n=== Basic Welding Calculator ===")

    try:
        price = float(input("Enter price per unit (₦): "))
        quantity = float(input("Enter quantity needed: "))
    except ValueError:
        print("\nInvalid input. Please enter numbers only.")
        input("Press Enter to return to menu...")
        return

    total = price * quantity

    print("\n--- Calculation Summary ---")
    print(f"Price per unit: ₦{price:,.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total cost: ₦{total:,.2f}")

    input("\nPress Enter to return to menu...")


def project_cost():
    print("\n=== Project Cost Calculator ===")

    try:
        material = float(input("Enter total material cost (₦): "))
        labor = float(input("Enter total labor cost (₦): "))
    except ValueError:
        print("\nInvalid input. Please enter numbers only.")
        input("Press Enter to return to menu...")
        return

    base = material + labor
    profit = base * 0.15      # 15% profit
    tax = base * 0.075        # 7.5% tax on base only
    final_price = base + profit + tax

    print("\n--- Project Summary ---")
    print(f"Base cost: ₦{base:,.2f}")
    print(f"Profit (15%): ₦{profit:,.2f}")
    print(f"Tax (7.5% on base): ₦{tax:,.2f}")
    print(f"Final price to charge: ₦{final_price:,.2f}")

    input("\nPress Enter to return to menu...")


def daily_log():
    print("\n=== Daily Welding Log ===")

    job = input("Enter job name: ")

    try:
        earnings = float(input("Enter earnings (₦): "))
    except ValueError:
        print("\nInvalid input. Please enter numbers only.")
        input("Press Enter to return to menu...")
        return

    # Save to file
    with open("welding_log.txt", "a") as file:
        file.write(f"{job} - ₦{earnings:,.2f}\n")

    print("\nJob saved successfully!")
    input("Press Enter to return to menu...")


while True:
    print("\n==== Moses Welding Tools ====")
    print("1. Basic Welding Calculator")
    print("2. Project Cost Calculator")
    print("3. Daily Welding Log")
    print("4. Moses Welding Calculator V2")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        basic_calculator()
    elif choice == "2":
        project_cost()
    elif choice == "3":
        daily_log()
    elif choice == "4":
        welding_calculator_v2()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option selected. Try again.")