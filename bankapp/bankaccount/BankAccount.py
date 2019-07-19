from abc import ABC, abstractmethod


class BankAccount(ABC):

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def transfer(self):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def get_account_number(self):
        pass

    @abstractmethod
    def get_transactions(self):
        pass
