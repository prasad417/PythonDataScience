from enum import Enum, unique, auto


@unique
class AccountType(Enum):
    SAVINGS_ACCOUNT = 'Savings Account'
    CHECKING_ACCOUNT = 'Checking Account'
    CERTIFICATE_OF_DEPOSIT = 'CD'
    PERSONAL_CREDIT_CARD = auto()
    BUSINESS_CREDIT_CARD = auto()
    MONEY_MARKET = 'Money Market'
