from bankapp.bankaccount.BankAccount import BankAccount


class CurrentAccount(BankAccount):

    def __init__(self, bank_account_type, bank_account_number, bank_account_status):
        self.balance = 0
        self.bank_account_type = bank_account_type
        self.bank_account_number = bank_account_number
        self.bank_account_status = bank_account_status

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited: ", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient funds.")

    def transfer(self):
        pass

    def get_balance(self):
        pass

    def get_account_number(self):
        pass

    def get_transactions(self):
        pass
