from bankapp.bank.Bank import Bank
from bankapp.address.Address import Address
from bankapp.bankaccount.CertificateOfDeposit import CertificateOfDeposit
from bankapp.bankaccount.CheckingAccount import CheckingAccount
from bankapp.bankaccount.SavingsAccount import SavingsAccount
from bankapp.bankcustomer.Customer import Customer
from bankapp.bankcustomer.Identification import Identification
from bankapp.bankcustomer.PersonalInformation import PersonalInformation
import json


class MainClass:

    bank = Bank()
    bank.get_bank_details()

    personal_info = PersonalInformation('Ryan', '', 'Beck', '11/28/1986', 'email@email.com', '1234567890', 'Male')
    address = Address('4101 W 98th', '101', 'Minneapolis', 'MN', '55437')
    identification = Identification('MN1234567890', '11/22', '123456789')
    customer = Customer(personal_info, address, identification)

    ca = CheckingAccount()
    customer.open_bank_account(ca)

    sa = SavingsAccount()
    customer.open_bank_account(sa)

    customer1 = Customer(personal_info, address, identification)

    ca = CheckingAccount()
    customer1.open_bank_account(ca)

    sa = SavingsAccount()
    customer1.open_bank_account(sa)

    cd = CertificateOfDeposit()
    customer.open_bank_account(cd)
    print('Test')

