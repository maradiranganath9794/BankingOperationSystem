class BankAccount:

    def __init__(self,current_balance):
       self.current_balance = current_balance
       print("Account is created Sucessfully with initial balance of " + str(self.current_balance))

    def Checkbalance(self):
        print("Net available balance = " + str(self.current_balance))
    def deposit(self,amount):
        self.current_balance = self.current_balance + amount
        print("Your account has been credited with " + str(amount))


    def Withdraw(self,amount):

        if self.current_balance >= amount:
            self.current_balance -= amount
            print("Your account is debitted with " + str(amount))

        else:
            print("Insufficient Balance")

    def Transfer(self,recipient,amount):
        self.Withdraw(amount)
        recipient.deposit(amount)

