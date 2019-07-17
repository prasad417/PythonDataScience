from abc import ABC, abstractmethod


class BankOperations(ABC):

    @abstractmethod
    def open_bank_account(self):
        pass

    @abstractmethod
    def deposit_to_bank_account(self):
        pass

    @abstractmethod
    def withdraw_from_bank_account(self):
        pass

    @abstractmethod
    def transfer_from_bank_account(self):
        pass
