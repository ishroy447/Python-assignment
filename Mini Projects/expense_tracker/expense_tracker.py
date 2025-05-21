import json
from datetime import datetime, timedelta
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.filename = "expenses.json"
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.expenses = json.load(file)

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        expense = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "amount": float(amount),
            "category": category,
            "description": description
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def get_weekly_summary(self):
        today = datetime.now()
        week_ago = today - timedelta(days=7)
        
        weekly_expenses = [
            exp for exp in self.expenses
            if datetime.strptime(exp["date"], "%Y-%m-%d") >= week_ago
        ]

        total = sum(exp["amount"] for exp in weekly_expenses)
        categories = {}
        
        for exp in weekly_expenses:
            category = exp["category"]
            if category not in categories:
                categories[category] = 0
            categories[category] += exp["amount"]

        print("\nWeekly Summary:")
        print(f"Total expenses: ${total:.2f}")
        print("\nExpenses by category:")
        for category, amount in categories.items():
            print(f"{category}: ${amount:.2f}")

    def display_all_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        print("\nAll Expenses:")
        for exp in self.expenses:
            print(f"Date: {exp['date']}")
            print(f"Amount: ${exp['amount']:.2f}")
            print(f"Category: {exp['category']}")
            print(f"Description: {exp['description']}")
            print("-" * 30)

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Weekly Summary")
        print("3. View All Expenses")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            amount = input("Enter amount: $")
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
        
        elif choice == "2":
            tracker.get_weekly_summary()
        
        elif choice == "3":
            tracker.display_all_expenses()
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 