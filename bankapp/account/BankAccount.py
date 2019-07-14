from bankapp.account.BankOperations import BankOperations
import uuid


class BankAccount(BankOperations):
    def __init__(self, bank_account_type):
        self.balance = 0
        self.bank_account_type = bank_account_type

    def open_bank_account(self):
        bank_account_no = uuid.uuid4().hex.upper()
        print(f'New {self.bank_account_type} created. Account number is: {bank_account_no}')
        return bank_account_no

    def deposit_to_bank_account(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited: ", amount)

    def withdraw_from_bank_account(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient funds.")
