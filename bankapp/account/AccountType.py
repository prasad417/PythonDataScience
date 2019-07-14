from enum import Enum, unique, auto


@unique
class AccountType(Enum):
    PERSONAL_SAVINGS_ACCOUNT = auto()
    PERSONAL_CHECKING_ACCOUNT = auto()
    BUSINESS_SAVINGS_ACCOUNT = auto()
    BUSINESS_CHECKING_ACCOUNT = auto()
    PERSONAL_CREDIT_CARD_ACCOUNT = auto()
    BUSINESS_CREDIT_CARD_ACCOUNT = auto()
