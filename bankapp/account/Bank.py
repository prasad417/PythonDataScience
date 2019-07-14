from abc import ABC, abstractmethod


class Bank(ABC):

    @abstractmethod
    def create_bank_account(self):
        pass

    @abstractmethod
    def deposit_to_bank_account(self):
        pass

    @abstractmethod
    def withdraw_from_bank_account(self):
        pass
