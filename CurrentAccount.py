from BankAccount import BankAccount

class CurrentAccount(BankAccount):

    def __init__(self,current_balance):
        super().__init__(current_balance)
    def Withdraw(self,amount):
        if self.current_balance >= amount + 200:
            self.current_balance -= amount + 200

            print("Your Account is debitted with " + str(amount))

        else:
            print("Insufficient Balance")

    def transfer(self,recipient,amount):

        if self.current_balance >= amount + 200:
            self.current_balance -= amount + 200
            recipient.deposit(amount)

            print("your account is debitted with " + str(amount))
            print("charges INR 200 as a fee")

