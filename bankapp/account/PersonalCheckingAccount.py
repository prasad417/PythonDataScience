from bankapp.account.BankAccount import BankAccount


class PersonalCheckingAccount(BankAccount):

    def __init__(self, bank_customer):
        self.bank_customer = bank_customer
        super(PersonalCheckingAccount, self).__init__(self.bank_customer)
        self.balance = 12000
