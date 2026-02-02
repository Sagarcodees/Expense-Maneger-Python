import os

class Expense:
    def __init__(self, date, name, price):
        self.date = date
        self.name = name
        self.price = price

    def save_to_file(self):
        try:
            with open("expenses.txt", "a") as f:
                f.write(f"{self.date}|{self.name}|{self.price}\n") 
            print("Expense Saved successfully!")
        except Exception as e:
            print(f"Error saving file: {e}")

while True:
    print("\n--- OOP EXPENSE MANAGER ---")
    print("1. Add Expense")
    print("2. View Total")
    print("3. View History")
    print("4. Exit")
    
    try:
        choice = int(input('Enter menu num: '))
    except :
        print("Please enter a valid number.")
        continue

    if choice == 1:
        while True:
            print("\n-- New Entry --")
            date = input("enter date as dd/mm/yyyy: ")
            item_name = input("Expense on: ")
            
            try:
                price = int(input("Amount: "))
                my_expense = Expense(date, item_name, price)
                my_expense.save_to_file()
                
            except :
                print("Invalid amount! Please enter a number.")

            cont = input("Enter '2' to go back, or any key to add more: ")
            if cont == '2':
                break

    elif choice == 2:
        if not os.path.exists("expenses.txt"):
            print("No expenses found yet!")
            continue

        try:
            total_sum = 0
            with open('expenses.txt', 'r') as f:
                for line in f:
                    if '|' in line: 
                        parts = line.strip().split('|')
                        cost = int(parts[2])
                        total_sum += cost
            
            print(f"Total Spent: ₹{total_sum}")
        except Exception as e:
            print(f"Error reading total: {e}")

    elif choice == 3:
        if not os.path.exists("expenses.txt"):
            print("No history found.")
            continue

        try:
            print("\n--- YOUR HISTORY ---")
            with open('expenses.txt', 'r') as f:
                for line in f:
                    if '|' in line:
                        print(line.strip())
        except Exception as e:
            print(f"Error reading history: {e}")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid input")