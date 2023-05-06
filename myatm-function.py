"""
Functionalities of ATM
1) Withdraw
2) Bank Statement
3) Current Balance
4) Pin Change
5) Deposit  (not every ATM support)

"""

def display_choices():
    print("We provide following functionalities")
    print("1) Withdraw")
    print("2) Bank Statement")
    print("3) Current Balance")
    print("4) Pin Change")


def choose_choice():
    display_choices()
    # It will get input from user
    choice = int(input("Please select a choice: "))
    if choice == 1:
        withdraw_money()
    elif choice == 2:
        display_bank_status()
    elif choice == 3:
        display_current_balance()
    elif choice == 4:
        change_pin()
    else:
        print("Wrong Choice")


def withdraw_money():
    print("Withdraw")
    withdraw_money = int(input("Enter amount: "))
    remain = balance - withdraw_money
    print("You have withdrawed", withdraw_money)
    print("Your remaining balance is", remain)
    display_bank_status()
    


def display_bank_status():
    print("Bank Statement")
    print("Your last 5 transactions are", last_transactions)


def display_current_balance():
    print("Current Balance")
    print("Your current balance is ", balance)


def change_pin():
    print("Pin Change")
    new_pin = int(input("Please enter your new pin"))
    print("Your new pin is changed to", new_pin)


balance = 500000
last_transactions = [10000, 20000, 100, 500, 2500]

choose_choice()