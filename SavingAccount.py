from BankAccount import BankAccount
class SavingAccount(BankAccount):
    def deposit(self,amount):
        super().deposit(amount)
        self.current_balance += amount * 0.03
        print(f"Added interest to Account New Balance: {self.current_balance}")


