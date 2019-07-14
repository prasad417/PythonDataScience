from bankapp.account.BankAccount import BankAccount


class PersonalCheckingAccount(BankAccount):

    def __init__(self):
        self.bank_account_type = 'Personal Checking Account'
        super(PersonalCheckingAccount, self).__init__(self.bank_account_type)
        self.balance = 12000
