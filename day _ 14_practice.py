# Write a program to update credits and balance of the user?

class Account:
    total_balance = 100000
    account_no = 2395873995839
    def __init__(self):
        pass

    def credits(self , deposite):
        self.total_balance = self.total_balance + deposite

    def debits(self , withdraw):
         self.total_balance = self.total_balance - withdraw

    def print_balance(self):
        print("Total Balance: ", self.total_balance)

acount = Account()
acount.print_balance()
acount.credits(20000)
print("The total balane after deposite is>>> : ")
acount.print_balance()
acount.debits(30000)
acount.print_balance()
