from bankapp.account.BusinessCheckingAccount import BusinessCheckingAccount
from bankapp.account.BusinessSavingsAccount import BusinessSavingsAccount
from bankapp.account.PersonalCheckingAccount import PersonalCheckingAccount
from bankapp.account.PersonalSavingsAccount import PersonalSavingsAccount
from bankapp.bankcustomer.BankCustomer import Customer
from bankapp.bankcustomer.CustomerAccount import CustomerAccount
from bankapp.bankcustomer.CustomerAddress import CustomerAddress
from bankapp.bankcustomer.CustomerIdentification import CustomerIdentification
from bankapp.bankcustomer.CustomerPersonalInformation import CustomerPersonalInformation
import json


class CreateAccount:

    customers = []

    customer_personal_info = CustomerPersonalInformation('first', '', 'last', '11/28/1986', 'email@email.com', '1234567890', 'Male')
    customer_address_info = CustomerAddress('4101 W 98th', '101', 'Minneapolis', 'MN', '55437')
    customer_identification = CustomerIdentification('MN1234567890', '11/22', '123456789')
    customer_account = CustomerAccount()
    customer1 = Customer(customer_personal_info, customer_address_info, customer_identification, customer_account)

    bca = BusinessCheckingAccount(customer1)
    bca.open_bank_account()
    print(json.dumps(customer_personal_info.__dict__))
    print(json.dumps(customer_address_info.__dict__))
    print(json.dumps(customer_identification.__dict__))
    print(json.dumps(customer_account.__dict__, default=str))

    customers.append(customer1)
    print(json.dumps(customer1.__dict__, default=str))
    # bsa = BusinessSavingsAccount()
    # bank_account_number = bsa.open_bank_account()
    # customer2 = Customer(customer_personal_info, customer_address_info, customer_identification, bank_account_number)
    #
    # pca = PersonalCheckingAccount()
    # bank_account_number = pca.open_bank_account()
    # customer3 = Customer(customer_personal_info, customer_address_info, customer_identification, bank_account_number)
    #
    # psa = PersonalSavingsAccount()
    # bank_account_number = psa.open_bank_account()
    # customer4 = Customer(customer_personal_info, customer_address_info, customer_identification, bank_account_number)

    # print(customer1, customer2, customer3, customer4)
