from bankapp.address.Address import Address


class Bank:

    accounts = {}
    customers = set()
    # bank_name
    # bank_routing_number Int
    # bank_address Address
    # show_bank_routing_number()
    # add_account()
    # remove_account()
    # add_customer()
    # remove_customer()

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

    def add_account(self, account_type, account_number):
        self.accounts[account_number] = account_type

    def remove_account(self):
        pass

    def get_all_accounts(self):
        print(self.accounts)

    def add_customer(self, customer_id):
        self.customers.add(customer_id)

    def remove_customer(self):
        pass

    def get_all_customers(self):
        print(self.customers)
    # @property
    # def bank_name(self):
    #     return self.__bank_name
    #
    # @bank_name.setter
    # def bank_name(self, bank_name):
    #     self.__bank_name = bank_name
