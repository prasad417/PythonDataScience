from bankapp.address.Address import Address


class Bank:

    accounts = {}
    customers = set()
    # bank_name
    # bank_routing_number Int
    # bank_address Address
    # get_bank_details()
    # show_bank_routing_number()

    def __init__(self):
        self.bank_name = 'Test Bank'
        self.bank_routing_number = '231130000'
        self.bank_address = Address('41 N 3rd St', '', 'Minneapolis', 'MN', '55401')

    def get_bank_details(self):
        print(f'Bank name: {self.bank_name}\n Routing number: {self.bank_routing_number}\n '
              f'Address: {self.bank_address.address_line1}, {self.bank_address.address_line2},'
              f'{self.bank_address.city}, {self.bank_address.state}, {self.bank_address.zip}')

    def get_bank_name(self):
        print(self.bank_name)

    def get_bank_routing_number(self):
        print(self.bank_routing_number)

    def get_bank_address(self):
        print(vars(self.bank_address))

    # @property
    # def bank_name(self):
    #     return self.__bank_name
    #
    # @bank_name.setter
    # def bank_name(self, bank_name):
    #     self.__bank_name = bank_name
