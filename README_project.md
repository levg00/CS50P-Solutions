# DEPOSIT MANAGER
#### Video Demo:  https://youtu.be/P-Ue0A0f01Q
#### Description:

## What is Deposit Manager?
Deposit Manager is a command-line program that helps you track your money. It lets you record income and expenses, see your transaction history, and export your financial data to CSV files. Think of it as a simple digital notebook for your finances that lives in your terminal.

## Why I Built This
I wanted to create a financial tool that anyone could use without needing to learn complicated software. Many money tracking apps have too many features that most people don't need. Deposit Manager does just the essentials: record money coming in, record money going out, analytics and csv export

### The Basics
When you start the program, you see a prompt where you can type commands. There are only a few commands to learn, which makes it very easy to use.

### Adding Money
To record income, you can type either:
- `add $100 salary` (if you want to be formal)
- `+$100 salary` (if you want to be quick)

The program understands both ways. The word after the amount is optional but helpful for remembering what the money was for.

### Recording Expenses
To record spending, you can type either:
- `withdraw $50 food`
- `-$50 food`

Again, both work the same way. The description helps you remember what you spent money on.

### Viewing Your History
You can see all your transactions by typing `print history`. This shows everything in the order it happened, with your running balance after each transaction.

### Seeing Sorted View
If you type `print sorted history`, you get a different view. It shows your income in one column and expenses in another, sorted from largest to smallest amount. This helps you quickly see your biggest transactions.

### Exporting Data
When you type `export csv`, the program creates a file called "history.csv" with all your transactions. If you type `export sorted csv`, it makes "sorted.csv" with transactions sorted by amount. Both files include helpful statistics like your average income and average spending.

### The Main File: deposit.py
This file contains everything the program needs to work. Here's what each part does:

**Global Variables**
- `balance` - keeps track of your current money total
- `history` - stores all your transactions as a list

**Main Function**
This is where the program starts. It waits for your commands in a loop until you type "exit".

**Adding Money Function**
When you type an add command, this function:
1. Figures out if you used "add $" or "+$"
2. Separates the amount from the description
3. Converts the amount to a number
4. Updates your balance
5. Saves the transaction to history
6. Shows you the new balance

**Withdrawing Money Function**
This works almost the same as adding money, but subtracts from your balance instead of adding.

**Print History Function**
This goes through your transaction history and displays each one with a number, the amount, description, and balance after that transaction.

**Print Sorted Function**
This is more complex. It:
1. Separates income and expense transactions
2. Sorts each group by amount (biggest first)
3. Displays them side by side in two columns
4. Makes sure the columns line up neatly

**Export Functions**
These create CSV files that spreadsheet programs can open. They include:
- All your transactions
- Your balance after each transaction
- Statistics at the bottom

### Testing File: test_simple.py
This file checks that the main functions work correctly.

### Why Global Variables?
I used global variables for balance and history because this is a small program that runs in one session. It made the code simpler to write and understand.

### Why Multiple Command Formats?
People have different preferences. Some like typing full words, others like shortcuts. Supporting both "add $" and "+$" makes the program more flexible.

### Why Two Display Modes?
The regular history view is good for seeing what happened when. The sorted view is better for understanding your spending patterns. Both are useful in different situations.

### Why CSV Export?
CSV files work with almost every spreadsheet program. This means you can do more advanced analysis in Excel, Google Sheets, or other programs if you want to.

### Formatting the Sorted Display
Making the two columns line up properly was tricky. I used Python's string formatting to ensure everything stays aligned

### Error Handling
I added try-except blocks to catch common errors and show helpful messages instead of scary Python error codes.
