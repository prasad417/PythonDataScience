from bankapp.bankaccount.AccountType import AccountType


class CustomerAccount:
    def __init__(self, bank_account_type=AccountType.CHECKING_ACCOUNT, bank_account_number=''):
        self.bank_account_type = bank_account_type
        self.bank_account_number = bank_account_number
