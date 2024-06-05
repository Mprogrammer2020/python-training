'''
Task: Create a simple ATM machine program, where user can:
1) Create an account (Open user account and set initial mininum balance to Rs.1000)
2) Deposit Money
3) Withdraw Money
4) Check Balance
Test Case:
1. User can only choose from '1', '2', '3' or '4'
2. User need to enter their account number for deposit, withdraw and check balance
3. User is required to have Rs.1000 minimum balance in their account

# updates that need to be done
1) Generate automatic 11 digit account number for new account.
2) After the account genration, user need to set the 4 digit pin for the account.
3) Add fifth option cahnge PIN
5) IF user enetr any wrong input at any step, it should ask user to enetr correct input insted of going on first step.
6) Given user an option to cancel the operation,  which will lead user to intial step.
'''
import random

def generate_account_number():
    return ''.join(random.choices('0123456789', k=11))

def deposit(account, amount):
    try:
        amount = int(amount)
        account['balance'] += amount
        print("Deposit successful. New balance: Rs.", account['balance'])
    except ValueError:
        print("Enter Amount.")

def withdraw(account, amount):
    try:
        amount = int(amount)
        if account['balance'] - amount >= 1000:
            account['balance']= amount
            print("Withdrawal successful. New balance:", account['balance'])
        else:
            print("Insufficient balance. Minimum balance of Rs.1000 must be maintained.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

def check_balance(account):
    print("Your current balance is Rs.", account['balance'])

def change_pin(account, new_pin):
    account['pin'] = new_pin
    print("PIN changed successfully.")

def is_numeric(text):
    return text.isdigit()

def main():
    accounts = {}

    while True:
        print("1. Open Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Change PIN")

        choice = input("Enter your choice 1 to 5: ")

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please choose from 1 to 5.")
            continue

        if choice == '1':
            account_number = generate_account_number()
            while True:
                pin = input("Enter your 4 digit PIN: ")
                if is_numeric(pin) and len(pin) == 4:
                    break
                else:
                    print("Invalid PIN. Please enter a 4-digit numeric PIN.")
            balance = 1000
            accounts[account_number] = {'pin': pin, 'balance': balance}
            print("Account created successfully. Your account number is:", account_number)

        elif choice in ['2', '3', '4', '5']:
            while True:
                account_number = input("Enter your account number or type cancel: ")
                if account_number.lower() == 'cancel':
                    break

                account = accounts.get(account_number)
                if not account:
                    print("Invalid account number. Please try again.")
                    continue

                pin = input("Enter your PIN  or type cancel: ")
                if pin.lower()== 'cancel':
                  break
                if not is_numeric(pin):
                    print("Invalid PIN. Please enter only numeric digits.")
                    continue

                if pin != account['pin']:
                    print("Invalid PIN. Please try again.")
                    continue
               
               #  deposit, withdraw, check balance, change pin
                if choice == '2':
                    while True:
                        amount = input("Enter amount to deposit or type cancel: ")
                        if amount.lower() == 'cancel':
                            break
                        elif is_numeric(amount):
                            deposit(account, amount)
                            break
                        else:
                            print("Invalid amount. Please enter a numeric value.")
                elif choice == '3':
                    while True:
                        amount = input("Enter amount to withdraw or type cancel: ")
                        if amount.lower() == 'cancel':
                            break
                        elif is_numeric(amount):
                            withdraw(account, amount)
                            break
                        else:
                            print("Invalid amount. Please enter a numeric value.")
                elif choice == '4':
                    check_balance(account)
                elif choice == '5':
                    while True:
                        new_pin = input("Enter your new 4 digit PIN or type cancel): ")
                        if new_pin.lower() == 'cancel':
                            break
                        elif is_numeric(new_pin) and len(new_pin) == 4:
                            change_pin(account, new_pin)
                            break
                        else:
                            print("Invalid PIN. Please enter a 4-digit numeric PIN.")              
                         
                break  
main()