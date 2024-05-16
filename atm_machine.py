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
'''
def create_account(accounts):
    acc_num = input("Enter a new account number: ")
    if acc_num in accounts:
        print("Account already exists.")
    else:
        accounts[acc_num] = 1000
        print(f"Account {acc_num} created with initial balance of Rs.1000")
        
def deposit_money(accounts):
    acc_num = input("Enter your account number: ")
    if acc_num not in accounts:
        print("Account does not exist.")
        return
    amount = int(input("Enter amount to deposit: "))
    accounts[acc_num] += amount     
    print(f"Rs.{amount} deposited successfully. Current Balance: Rs.{accounts[acc_num]}")

def withdraw_money(accounts):
    acc_num = input("Enter your account number: ")
    if acc_num not in accounts:
        print("Account does not exist.")
        return
    amount = int(input("Enter amount to withdraw: "))
    if accounts[acc_num] - amount < 1000:
        print("Insufficient balance. Minimum balance of Rs.1000 must be maintained.")
    else:
        accounts[acc_num] -= amount
        print(f"Rs.{amount} withdrawn successfully. Current Balance: Rs.{accounts[acc_num]}")

def check_balance(accounts):
    acc_num =int(input("Enter your account number: "))
    if acc_num not in accounts:
        print("Account does not exist.")
    else:
        print(f"Current Balance: Rs.{accounts[acc_num]}")

def main():
    accounts = {}
    while True:
        print("Choose an option:")
        print("1. Create an account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit_money(accounts)
        elif choice == '3':
            withdraw_money(accounts)
        elif choice == '4':
            check_balance(accounts)
        elif choice == '5':
                print("Thank For using This Bank")
                break
        else:
            print("Invalid choice. Please choose from '1', '2', '3', or '4'.")
main()

