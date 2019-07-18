from bankapp.Bank import Bank
from bankapp.address.Address import Address
from bankapp.bankaccount.CheckingAccount import CheckingAccount
from bankapp.bankaccount.SavingsAccount import SavingsAccount
from bankapp.bankcustomer.Customer import Customer
from bankapp.bankcustomer.Identification import Identification
from bankapp.bankcustomer.PersonalInformation import PersonalInformation


class MainClass:

    bank = Bank()
    bank.get_bank_details()

    customer_personal_info = PersonalInformation('Ryan', '', 'Beck', '11/28/1986', 'email@email.com', '1234567890', 'Male')
    customer_address = Address('4101 W 98th', '101', 'Minneapolis', 'MN', '55437')
    customer_identification = Identification('MN1234567890', '11/22', '123456789')
    customer = Customer(customer_personal_info, customer_address, customer_identification)

    ca = CheckingAccount(customer)
    ca.open_bank_account()

    sa = SavingsAccount(customer)
    sa.open_bank_account()

    customer1 = Customer(customer_personal_info, customer_address, customer_identification)

    ca = CheckingAccount(customer1)
    ca.open_bank_account()

    sa = SavingsAccount(customer1)
    sa.open_bank_account()

    bank.get_all_accounts()
    bank.get_all_customers()
    print('Test')

