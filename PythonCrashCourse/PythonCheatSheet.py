import keyword

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(f'{color.BOLD}Hello! Welcome to python course.{color.END}')
print('                                                                         ')
print(f'{color.BOLD}==================================={color.END}')
print(f'{color.BOLD}Python has 33 Keywords{color.END}')
print(f'{color.BOLD}==================================={color.END}')
print(keyword.kwlist)
print('                                                                         ')
print('                                                                         ')
print(f'{color.BOLD}==================================={color.END}')
print(f'{color.BOLD}Python has 14 Data Types{color.END}')
print(f'{color.BOLD}==================================={color.END}')
print(f'''{color.BOLD}Fundamental data types:{color.END} 'int', 'float', 'complex', 'bool', 'str' ''')
print(f'''{color.BOLD}Collection related data types:{color.END} 'list', 'tuple', 'set', 'frozenset', 'dict', 'bytes', 'bytearray', 'range' ''')
print(f'{color.BOLD}Other data types: {color.END}None')
print('                                                                         ')
print('                                                                         ')
itemName = '4K Tv'
itemQuantity = 4
itemPrice = 10.99e17
isEnergySaver = False
binaryFormat = 0B1111
octalFormat = 0O123
hexaDecimalFormat = 0XFACE23
complexNumberFormat = 10 + 20j
print(f'{color.BOLD}==================================={color.END}')
print(f'{color.BOLD}Data type \'String\' immutable{color.END}')
print(f'{color.BOLD}==================================={color.END}')
print(f'Type of object is type(o) {type(itemName)}, {itemName}')
print(f'Address of the object is id(o) {id(itemName)}')
print(f'{color.BOLD}==================================={color.END}')
print(f'{color.BOLD}String Formatting and Slice{color.END}')
print(f'{color.BOLD}==================================={color.END}')
name = 'test'
print(f'{name}, name[1:3], {name[1:3]}')
print(f'{name}, name[1:], {name[1:]}')
print(f'{name}, name[:2], {name[:2]}')
print(f'{name}, name[0:-2], {name[0:-2]}')
print(f'{name}, name[-1], {name[-1]}')
print(f'{color.BOLD}========================================================={color.END}')
print(f'{color.BOLD}Data type \'Int\' immutable, binary, octal, hexa decimal{color.END}')
print(f'{color.BOLD}========================================================={color.END}')
print(f'Type of object is type(o) {type(itemQuantity)}, {itemQuantity}')
print(f'When a number is prefixed with \'0b\' or \'0B\' is called binary ex:0B1111, {binaryFormat}')
print(f'When a number is prefixed with \'0o\' or \'0O\' is called octal ex:0O123, {octalFormat}')
print(f'When a number is prefixed with \'0x\' or \'0X\' is called hexa decimal ex:0XFACE23, {hexaDecimalFormat}')
print(f'{color.BOLD}==================================={color.END}')
print(f'{color.BOLD}Data type \'float\' immutable{color.END}')
print(f'{color.BOLD}==================================={color.END}')
print(f'Type of object is type(o) {type(itemPrice)}, {itemPrice}')
print(f'{color.BOLD}==================================={color.END}')
print(f'{color.BOLD}Data type \'bool\' immutable{color.END}')
print(f'{color.BOLD}==================================={color.END}')
print(f'Type of object is type(o) {type(isEnergySaver)}, {isEnergySaver}')
print(f'{color.BOLD}==================================={color.END}')
print(f'{color.BOLD}Data type \'complex\' immutable')
print(f'{color.BOLD}==================================={color.END}')
print(f'Type of object is type(o) {type(complexNumberFormat)}, real part of {complexNumberFormat}', complexNumberFormat.real)
print(f'Type of object is type(o) {type(complexNumberFormat)}, imaginary part of {complexNumberFormat}', complexNumberFormat.imag)
print(f'Defining complex(10, 10.2) is {complex(10, 10.2)}')
print(f'Defining complex with string only takes real part, complex("10") is {complex("10")}')
print(f'Defining complex(25) is {complex(25)}')
#print(f'{color.BOLD}==================================={color.END}')
#print(f'{color.BOLD}Input from user{color.END}')
#print(f'{color.BOLD}==================================={color.END}')
#userName = input('What is your name?')
#print('Welcome ', userName)
#print('                                                                         ')
#print('                                                                         ')
print(f'{color.BOLD}==================================={color.END}')
print(f'''{color.BOLD}Data type 'list': [], 
            order is preserved , 
            allows duplicate objects [10, 10], 
            hetrogenous objects[10, 'list', True], 
            growable in nature,
            mutable{color.END}''')
print('==================================={color.END}')
list = [10, 'a', 20, 'b', 10, True]
print(f'Type of object is type(o) {list}, {type(list)}')
print(f'{list}, access list with index list[0], {list[0]}')
print(f'{list}, slice list with index list[0: 3], {list[0: 3]}')
print(f'{list}, slice list with index list[-1], {list[-1]}')
print(f'Address of the object is id(o) {list}, {id(list)}')
list[0] = 50
print(f'Assign first index with 50 to {list}')
print(f'Address of the object is id(o) {list}, {id(list)}')
print('                                                                         ')
print('                                                                         ')
print(f'{color.BOLD}==================================={color.END}')
print(f'{color.BOLD}Precedence{color.END}')
print(f'{color.BOLD}==================================={color.END}')
print('()   Parentheses')
print('**   Exponent')
print('Multiplication or Division')
print('Addition or Subtraction')
print('+x, -x, ~x	Unary plus, Unary minus, Bitwise NOT')
print('*, /, //, %  Multiplication, Division, Floor division, Modulus')
print('+, - Addition, Subtraction')
print('<<, >>	Bitwise shift operators')
print('&	Bitwise AND')
print('^	Bitwise XOR')
print('|	Bitwise OR')
print('==, !=, >, >=, <, <=, is, is not, in, not in	Comparisions, Identity, Membership operators')
print('not	Logical NOT')
print('and	Logical AND')
print('or	Logical OR')
print(f'{color.BOLD}Example:{color.END}')
print(f'(3 + 3) * 2 ** 3 - 3 + 10 is {(3 + 3) * 2 ** 3 - 3 + 10}')
print('                                                                         ')
print('                                                                         ')
print(f'{color.BOLD}==================================={color.END}')
print(f'{color.BOLD}Conditional \'If\' Statement{color.END}')
print(f'{color.BOLD}==================================={color.END}')
print(f'''{color.BOLD}if type(itemName) is int:
    print('Type is Integer')
elif type(itemName) is str:
    print('Type is String.')
else:
    print('Couldn\'t find type'){color.END}''')
print('                                                                         ')
print('                                                                         ')
