from BankAccount import BankAccount
from SavingAccount import SavingAccount
from CurrentAccount import CurrentAccount

class test:
    B1 = BankAccount(500)
    B2 = BankAccount(200)
    B1.Withdraw(200)
    B2.deposit(1000)
    B2.Transfer(B1,500)
    B1.Checkbalance()
    B2.Checkbalance()

    S1 = SavingAccount(2000)
    #S1.deposit(500)
    S1.deposit(500)
    S1.Checkbalance()

    S2 = CurrentAccount(2000)
    S2.deposit(500)
    S2.Withdraw(100)
    S2.Checkbalance()
    S2.transfer(S1,500)



    S1.Checkbalance()
    S2.Checkbalance()






