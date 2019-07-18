from bankapp.bankaccount.AccountType import AccountType
from bankapp.bankaccount.BankAccount import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self, bank_customer):
        self.bank_customer = bank_customer
        super(CheckingAccount, self).__init__(self.bank_customer, AccountType.CHECKING_ACCOUNT.name)
