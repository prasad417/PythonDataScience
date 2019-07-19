import uuid

from bankapp.bankaccount.AccountStatus import AccountStatus
from bankapp.bankaccount.AccountType import AccountType
from bankapp.bankaccount.CurrentAccount import CurrentAccount


class CheckingAccount(CurrentAccount):

    def __init__(self):
        super(CheckingAccount, self).__init__(AccountType.CHECKING_ACCOUNT.value, uuid.uuid4().hex.upper(),
                                              AccountStatus.ACTIVE.name)
