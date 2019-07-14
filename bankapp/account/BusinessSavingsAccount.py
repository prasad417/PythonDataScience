from bankapp.account.BankAccount import BankAccount


class BusinessSavingsAccount(BankAccount):

    def __init__(self):
        self.bank_account_type = 'Business Savings Account'
        super(BusinessSavingsAccount, self).__init__(self.bank_account_type)
        self.balance = 12000
