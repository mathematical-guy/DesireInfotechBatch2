"""
Functionalities of ATM
1) Withdraw
2) Bank Statement
3) Current Balance
4) Pin Change
5) Deposit  (not every ATM support)

"""

balance = 500000
last_transactions = [10000, 20000, 100, 500, 2500]

print("We provide following functionalities")
print("1) Withdraw")
print("2) Bank Statement")
print("3) Current Balance")
print("4) Pin Change")

choice = int(input("Please select a choice: "))

if choice == 1:
    print("Withdraw")
    withdraw_money = int(input("Enter amount: "))
    remain = balance - withdraw_money
    print("You have withdrawed", withdraw_money)
    print("Your remaining balance is", remain)
    

elif choice == 2:
    print("Bank Statement")
    print("Your last 5 transactions are", last_transactions)
elif choice == 3:
    print("Current Balance")
    print("Your current balance is ", balance)
else:
    print("Pin Change")
    new_pin = int(input("Please enter your new pin"))
    print("Your new pin is changed to", new_pin)
