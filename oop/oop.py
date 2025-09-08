class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accName):
        self.name = accName
        self.balance = initialAmount
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance}")

    def get_balance(self):
        print(f"Account '{self.name}' balance = ${self.balance}")
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(
            f"Deposited ${amount} to '{self.name}' account.\nNew balance = ${self.balance}")
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        print(
            f"Withdraw ${amount} from '{self.name}' account.\nNew balance = ${self.balance}")
        return self.balance

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print(f"\n************\n\nBeginning Transfer.. 🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complere! ✔\n\n************")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")


class InterestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()


class SavingAcct(InterestRewardsAcc):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interupted: {error}")
