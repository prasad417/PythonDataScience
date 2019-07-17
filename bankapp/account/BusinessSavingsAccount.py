from bankapp.account.BankAccount import BankAccount


class BusinessSavingsAccount(BankAccount):

    def __init__(self, bank_customer):
        self.bank_customer = bank_customer
        super(BusinessSavingsAccount, self).__init__(self.bank_customer)
        self.balance = 12000
