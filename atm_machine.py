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
    print("1. Create Account")
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
        account_number = input("Enter your account number or type to cancel: ")
        if account_number.lower()=='cancel':    
         break
        
        if not is_numeric(account_number):
          print("Invalid account number. Please enter only numeric digits.")
          continue

        pin = input("Enter your PIN: ")
        if not is_numeric(pin):
          print("Invalid PIN. Please enter only numeric digits.")
          continue

        account = accounts.get(account_number)
        if account is None:
          print("Invalid account number. Please try again.")
          continue

        if pin != account['pin']:
          print("Invalid PIN. Please try again.")
          continue

        #  deposit, withdraw, check balance, change pin
        if choice == '2':
          while True:
            amount = input("Enter amount to deposit: ")
            
            if is_numeric(amount):
              deposit(account, amount)
              break
            else:
              print("Invalid amount. Please enter a numeric value.")
        elif choice == '3':
          while True:
            amount = input("Enter amount to withdraw: ")
            if is_numeric(amount):
              withdraw(account, amount)
              break
            else:
              print("Invalid amount. Please enter a numeric value.")
        elif choice == '4':
          check_balance(account)
        elif choice == '5':
          while True:
            new_pin = input("Enter your new 4 digit PIN: ")
            if is_numeric(new_pin) and len(new_pin) == 4:
              change_pin(account, new_pin)
              break
            else:
              print("Invalid PIN. Please enter a 4-digit numeric PIN.")
        break  
    
main()
