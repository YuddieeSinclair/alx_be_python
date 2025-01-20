class BankAccount:


    def __init__(self, account_balance, initial_balance = 0):
        self.__account_balance = account_balance
        self.__initial_balance = initial_balance

    def deposit(self, amount):
        depos = self.__account_balance + amount
        return f"Deposited: ${amount}"
    
    def withdraw(self, amount):
        if amount > self.__account_balance:
            #print("insufficient funds")
            return False
        else:
            amount_withdrawn = self.__account_balance - amount
            #print(f"Withdrew: ${amount}")
            return True
    
    def display_balance(self):
        print(f"your current balance is {self.__account_balance}")
