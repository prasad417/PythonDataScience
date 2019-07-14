from bankapp.account.BankAccount import BankAccount


class PersonalSavingsAccount(BankAccount):

    def __init__(self):
        self.bank_account_type = 'Personal Savings Account'
        super(PersonalSavingsAccount, self).__init__(self.bank_account_type)
        self.balance = 12000
