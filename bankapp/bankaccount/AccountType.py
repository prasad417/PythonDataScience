from enum import Enum, unique, auto


@unique
class AccountType(Enum):
    SAVINGS_ACCOUNT = auto()
    CHECKING_ACCOUNT = auto()
    PERSONAL_CREDIT_CARD = auto()
    BUSINESS_CREDIT_CARD = auto()
    MONEY_MARKET = auto()
