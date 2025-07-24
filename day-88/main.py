expenses = []

def add_expense():
    title = input("Enter expense title: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    expenses.append({"title": title, "amount": amount})
    print("Expense added successfully.\n")

def show_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\n--- Expense List ---")
    total = 0
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx}. {exp['title']} - ${exp['amount']:.2f}")
        total += exp["amount"]
    print(f"Total Expense: ${total:.2f}\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
