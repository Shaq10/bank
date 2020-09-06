class BankAccount(object):
    balance = 0

    def __init__(self, name):
        self.name = name
      
    # return a message stating who the account belongs to,including the balance
    def __repr__(self):
        return "%s's account. Balance: $%.2f" % (self.name, self.balance)
      
    #prints just the user's balance
    def show_balance(self):
        print ("User's balance is: $%.2f" % self.balance)
      
    #method allowing deposits to bank account. User's balance incremented if deposit is more than zero
    def deposit(self, amount):
        if amount <= 0:
            print ("Amount is less than zero")
            return
        else:
            print ("$%.2f has been deposited" % amount)
            self.balance += amount
            self.show_balance()
    
    #method allowing withdrawals to be made if there's enough money in the account. User's balance also updated
    def withdraw(self, amount):
        if amount >= self.balance:
            "There is not enough money in your account"
            return
        else:
            print ("$%.2f has been withdrawn" % amount)
            self.balance -= amount
            self.show_balance()


#Test Bank Account created
my_account = BankAccount("Shaq") 
print (my_account) 
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print (my_account)

