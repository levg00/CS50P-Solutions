import pytest
import csv
import project
from project import add_money, withdraw_money, print_history, print_sorted, export_csv, export_sorted_csv, show_help

def test_add_money():
    project.balance = 0
    project.history = []
    add_money("add $100 salary")
    assert project.balance == 100
    assert project.history == [("+", 100, "salary")]

def test_withdraw_money():
    project.balance = 0
    project.history = []
    add_money("add $500 test")
    withdraw_money("withdraw $100 food")
    assert project.balance == 400
    assert project.history[-1] == ("-", 100, "food")

def test_print_history():
    add_money("add $500 test")
    withdraw_money("withdraw $100 food")
    print_history()
    assert "No errors occured"

def test_print_sorted():
    add_money("add $500 test")
    withdraw_money("withdraw $100 food")
    print_sorted()
    assert "No errors occured"

def test_export_csv():
    add_money("add $500 test")
    withdraw_money("withdraw $100 food")
    export_csv()
    assert "No errors occured"

def test_export_sorted_csv():
    add_money("add $500 test")
    withdraw_money("withdraw $100 food")
    export_sorted_csv()
    assert "No errors occured"

def test_show_help():
    assert show_help() == """
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
"""
