import uuid

from bankapp.bankaccount.AccountStatus import AccountStatus
from bankapp.bankaccount.AccountType import AccountType
from bankapp.bankaccount.CurrentAccount import CurrentAccount


class CertificateOfDeposit(CurrentAccount):

    def __init__(self):
        super(CertificateOfDeposit, self).__init__(AccountType.CERTIFICATE_OF_DEPOSIT.value, uuid.uuid4().hex.upper(),
                                                   AccountStatus.ACTIVE.name)
        self.balance = 12000
