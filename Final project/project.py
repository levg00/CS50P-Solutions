import csv
import sys

balance = 0
history = []

def main():
    print("Deposit Manager")
    print("Type 'help' for commands")

    while True:
        inp = input("> ").strip().lower()

        if inp.startswith(("add $", "+$")):
            add_money(inp)
        elif inp.startswith(("withdraw $", "-$")):
            withdraw_money(inp)
        elif inp == "export csv":
            export_csv()
        elif inp == "export sorted csv":
            export_sorted_csv()
        elif inp == "print history":
            print_history()
        elif inp == "print sorted history":
            print_sorted()
        elif inp == "help":
            print(show_help())
        elif inp == "exit":
            sys.exit()
        else:
            raise ValueError("Unknown command, see available commands via 'help'")

def add_money(inp):
    global balance, history
    try:
        if inp.startswith("add $"):
            data = inp[5:]
        else:
            data = inp[2:]

        parts = data.split(" ", 1)
        amount = float(parts[0])
        desc = parts[1] if len(parts) > 1 else ""

        balance += amount
        history.append(("+", amount, desc))
        print(f"+${amount} {desc} | Balance: ${balance}")
    except (ValueError, TypeError, IndexError):
        print("Error: Use 'add $100 item' or '+$100 item'")

def withdraw_money(inp):
    global balance, history
    try:
        if inp.startswith("withdraw $"):
            data = inp[10:]
        else:
            data = inp[2:]

        parts = data.split(" ", 1)
        amount = float(parts[0])
        desc = parts[1] if len(parts) > 1 else ""

        balance -= amount
        history.append(("-", amount, desc))
        print(f"-${amount} {desc} | Balance: ${balance}")
    except (ValueError, TypeError, IndexError):
        print("Error: Use 'withdraw $100 item' or '-$100 item'")

def print_history():
    if not history:
        print("No history")
        return

    print("\nHISTORY:")
    total = 0
    for i, (action, amount, desc) in enumerate(history, 1):
        if action == "+":
            total += amount
            print(f"{i}. +${amount} {desc} | Balance: ${total}")
        else:
            total -= amount
            print(f"{i}. -${amount} {desc} | Balance: ${total}")

def print_sorted():
    if not history:
        print("No history")
        return

    income = [(amount, desc) for action, amount, desc in history if action == "+"]
    expenses = [(amount, desc) for action, amount, desc in history if action == "-"]

    income.sort(reverse=True)
    expenses.sort(reverse=True)

    print("\nSORTED HISTORY:")
    print("INCOME          | EXPENSES")
    print("-" * 30)

    for i in range(max(len(income), len(expenses))):
        inc = f"+${income[i][0]} {income[i][1]}" if i < len(income) else ""
        exp = f"-${expenses[i][0]} {expenses[i][1]}" if i < len(expenses) else ""
        print(f"{inc:15} | {exp}")

def export_csv():
    if not history:
        print("No history")
        return

    with open("history.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Action", "Amount", "Description", "Balance"])

        total = 0
        for action, amount, desc in history:
            if action == '+':
                total += amount
            else:
                total -= amount
            writer.writerow([action, amount, desc, "$" + str(total)])

        income = [amount for action, amount, desc in history if action == "+"]
        expenses = [amount for action, amount, desc in history if action == "-"]

        writer.writerow([])
        writer.writerow(["FINAL BALANCE", '', '', "$" + str(balance)])
        writer.writerow(["Average Income", '', '', "$" + str(sum(income)/len(income) if income else 0)])
        writer.writerow(["Average Expense", '', '', "$" + str(sum(expenses)/len(expenses) if expenses else 0)])

    print("Exported: history.csv")

def export_sorted_csv():
    if not history:
        print("No history")
        return

    sorted_hist = sorted(history, key=lambda x: x[1], reverse=True)

    with open("sorted.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Action", "Amount", "Description"])

        for action, amount, desc in sorted_hist:
            writer.writerow([action, "$" + str(amount), desc])

        income = [amount for action, amount, desc in history if action == "+"]
        expenses = [amount for action, amount, desc in history if action == "-"]

        writer.writerow([])
        writer.writerow(["FINAL BALANCE", '',"$" + str(balance)])
        writer.writerow(["Average Income", '',"$" + str(sum(income)/len(income) if income else 0)])
        writer.writerow(["Average Expense", '',"$" + str(sum(expenses)/len(expenses) if expenses else 0)])

    print("Exported: sorted.csv")

def show_help():
    return("""
Commands:
add $100 item         - Add money
+$100 item            - Add money
withdraw $100 item    - Withdraw money
-$100 item            - Withdraw money
export csv            - Export to CSV
export sorted csv     - Export sorted to CSV
print history         - Show history
print sorted history  - Show sorted history
help                  - This help
exit                  - Exit
""")

if __name__ == "__main__":
    main()
