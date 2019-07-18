from bankapp.Bank import Bank
from bankapp.bankaccount.AccountStatus import AccountStatus
from bankapp.bankaccount.BankOperations import BankOperations
from bankapp.bankcustomer.Account import Account
import uuid


class BankAccount(BankOperations):

    def __init__(self, bank_customer, bank_account_type):
        self.balance = 0
        self.bank_customer = bank_customer
        self.bank_account_type = bank_account_type

    def open_bank_account(self):
        bank_account_number = uuid.uuid4().hex.upper()
        account = Account(self.bank_account_type, bank_account_number, AccountStatus.ACTIVE.name)
        self.bank_customer.accounts.append(account)
        bank = Bank()
        bank.add_account(self.bank_account_type, bank_account_number)
        bank.add_customer(self.bank_customer.id)

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
