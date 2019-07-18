import uuid

from bankapp.bankcustomer.Account import Account


class Customer:

    # customer_id String
    # first_name String
    # middle_name String
    # last_name String
    # email String
    # date_of_birth Date
    # gender String
    # phone_number int
    # address_line1 String
    # address_line2 String
    # city String
    # state String
    # zip int
    # identification_number String
    # identification_exp_date String
    # ssn int
    # get_name()
    # get_customer_id()

    def __init__(self, personal_info, address, identification):
        self.id = uuid.uuid4().hex.upper()
        self.personal_info = personal_info
        self.address = address
        self.identification = identification
        self.accounts = []

    def get_customer_name(self):
        print(f'{self.personal_info.first_name}, {self.personal_info.last_name}')

    def get_customer_id(self):
        print(self.id)
