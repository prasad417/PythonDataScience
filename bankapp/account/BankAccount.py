from bankapp.account.BankOperations import BankOperations
import uuid


class BankAccount(BankOperations):

    def __init__(self, bank_customer):
        self.balance = 0
        self.bank_customer = bank_customer

    def open_bank_account(self):
        self.bank_customer.customer_account.bank_account_number = uuid.uuid4().hex.upper()

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

    def transfer_from_bank_account(self):
        pass
