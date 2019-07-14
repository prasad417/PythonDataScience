from bankapp.account.BankAccount import BankAccount


class BusinessCheckingAccount(BankAccount):

    def __init__(self):
        self.bank_account_type = 'Business Checking Account'
        super(BusinessCheckingAccount, self).__init__(self.bank_account_type)
        self.balance = 12000
