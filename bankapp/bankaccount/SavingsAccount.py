from bankapp.bankaccount.AccountType import AccountType
from bankapp.bankaccount.BankAccount import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self, bank_customer):
        self.bank_customer = bank_customer
        super(SavingsAccount, self).__init__(self.bank_customer, AccountType.SAVINGS_ACCOUNT.name)
        self.balance = 12000
