from oop import *

John = BankAccount(1000, "John")
Sara = BankAccount(200, "Sara")

John.get_balance()
Sara.get_balance()
Sara.deposit(2000)

John.deposit(700)


Sara.withdraw(90)
John.withdraw(250)

John.transfer(600, Sara)

Jim = InterestRewardsAcc(800, "Jim")

Jim.get_balance()
Jim.deposit(200)
Jim.transfer(440, John)

Jim.withdraw(90)


Blaze = SavingAcct(300, "Blaze")

Blaze.get_balance()
Blaze.deposit(200)
Blaze.withdraw(100)
Blaze.transfer(300, Sara)
