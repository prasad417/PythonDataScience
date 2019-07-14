from enum import Enum, unique, auto


@unique
class AccountStatus(Enum):
    ACTIVE = auto()
    CLOSED = auto()