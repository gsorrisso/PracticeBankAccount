class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance 
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5    
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance:,}")# I want to add a whatever name is before the balance "joes balance"
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= 1 + self.int_rate
        return self 

# user_one = BankAccount(.05, 5000)
# user_two = BankAccount(.01, 1000)

# user_one.deposit(1000).deposit(1000).deposit(1000).withdraw(3000).yield_interest().display_account_info()
# user_two.deposit(1000).deposit(1000).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"User name is: {self.name}")
        self.account.display_account_info()

user_one = User("Joe", "JoeEmail")
user_two = User("Jane", "JaneEmail")

user_one.make_deposit(1000).display_user_balance()