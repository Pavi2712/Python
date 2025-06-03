#Globally 1000 is in account balance
account_balance = 1000 #This is at module level

def get_account_balance():
    """Returns the current account balance."""
    return account_balance

#This function takes a parameter new_balance and sets the global account_balance to the new value.
def set_account_balance(new_balance):
    """Sets a new value for the account balance."""
    global account_balance
    account_balance = new_balance

# Class to represent a user's bank account
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 500  # Default amount

    def deposit(self, amount): #Used to deposit the money into user account
        """Deposit money into the user's account."""
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount): #Withdraw money
        """Withdraw money from the user's account."""
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            return self.balance
        elif amount > self.balance:
            return "Insufficient funds"
        else:
            return "Invalid withdrawal amount"

# Function Scope
def deposit_to_global_account(amount):
    """Function to deposit money into the global account."""
    global account_balance
    if amount > 0:
        account_balance += amount
        return account_balance
    else:
        return "Invalid deposit amount"
