import keyword
from utils.Color import Color

print(f'{Color.BOLD}Hello! Welcome to python course.{Color.END}')
print('                                                                         ')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'{Color.BOLD}Python has 33 Keywords{Color.END}')
print(f'{Color.BOLD}==================================={Color.END}')
print(keyword.kwlist)
print('                                                                         ')
print('                                                                         ')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'{Color.BOLD}Python has 14 Data Types{Color.END}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'''{Color.BOLD}Fundamental data types:{Color.END} 'int', 'float', 'complex', 'bool', 'str' ''')
print(f'''{Color.BOLD}Collection related data types:{Color.END} 'list', 'tuple', 'set', 'frozenset', 'dict', 'bytes', 'bytearray', 'range' ''')
print(f'{Color.BOLD}Other data types: {Color.END}None')
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
print(f'{Color.BOLD}==================================={Color.END}')
print(f'{Color.BOLD}Data type \'String\' immutable{Color.END}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'Type of object is type(o) {type(itemName)}, {itemName}')
print(f'Address of the object is id(o) {id(itemName)}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'{Color.BOLD}String Formatting and Slice{Color.END}')
print(f'{Color.BOLD}==================================={Color.END}')
name = 'test'
print(f'{name}, name[1:3], {name[1:3]}')
print(f'{name}, name[1:], {name[1:]}')
print(f'{name}, name[:2], {name[:2]}')
print(f'{name}, name[0:-2], {name[0:-2]}')
print(f'{name}, name[-1], {name[-1]}')
print(f'{Color.BOLD}========================================================={Color.END}')
print(f'{Color.BOLD}Data type \'Int\' immutable, binary, octal, hexa decimal{Color.END}')
print(f'{Color.BOLD}========================================================={Color.END}')
print(f'Type of object is type(o) {type(itemQuantity)}, {itemQuantity}')
print(f'When a number is prefixed with \'0b\' or \'0B\' is called binary ex:0B1111, {binaryFormat}')
print(f'When a number is prefixed with \'0o\' or \'0O\' is called octal ex:0O123, {octalFormat}')
print(f'When a number is prefixed with \'0x\' or \'0X\' is called hexa decimal ex:0XFACE23, {hexaDecimalFormat}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'{Color.BOLD}Data type \'float\' immutable{Color.END}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'Type of object is type(o) {type(itemPrice)}, {itemPrice}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'{Color.BOLD}Data type \'bool\' immutable{Color.END}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'Type of object is type(o) {type(isEnergySaver)}, {isEnergySaver}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'{Color.BOLD}Data type \'complex\' immutable')
print(f'{Color.BOLD}==================================={Color.END}')
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
print(f'{Color.BOLD}==================================={Color.END}')
print(f'''{Color.BOLD}Data type 'list': [], 
            order is preserved , 
            allows duplicate objects [10, 10], 
            hetrogenous objects[10, 'list', True],
            growable in nature,
            mutable{Color.END}''')
print(f'{Color.BOLD}==================================={Color.END}')
list = [10, 'a', 20, 'b', 10, True]
print(f'Type of object is type(o) {list}, {type(list)}')
print(f'{list}, access list with index list[0], {list[0]}')
print(f'{list}, slice list with index list[0: 3], {list[0: 3]}')
print(f'{list}, slice list with index list[-1], {list[-1]}')
print(f'Address of the object is id(o) {list}, {id(list)}')
list[0] = 50
print(f'Assign first index with 50 to {list}')
print(f'Address of the object is id(o) {list}, {id(list)}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'''{Color.BOLD}Data type 'tuple': (), 
            order is preserved , 
            allows duplicate objects [10, 10], 
            hetrogenous objects[10, 'list', True],
            immutable
            single value tuple should end with ','{Color.END}''')
print(f'{Color.BOLD}==================================={Color.END}')
tupleDataType = (10, 'a', 20, 'b', 10, True)
print(f'Type of object is type(o) {tupleDataType}, {type(tupleDataType)}')
print(f'{tupleDataType}, access tuple with index tuple[0], {tupleDataType[0]}')
print(f'{tupleDataType}, slice tuple with index tuple[0: 3], {tupleDataType[0: 3]}')
print(f'{tupleDataType}, slice tuple with index tuple[-1], {tupleDataType[-1]}')
print(f'Address of the object is id(o) {tupleDataType}, {id(tupleDataType)}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'''{Color.BOLD}Data type 'set': 
            order is not preserved , 
            duplicate objects not allowed, 
            hetrogenous objects[10, 'list', True],
            mutable,
            growable in nature,
            indexing/slicing not applicable{Color.END}''')
print(f'{Color.BOLD}==================================={Color.END}')
setDataType = {20, 'a', 20, 'b', 10, True}
print(f'Type of object is type(o) {setDataType}, {type(setDataType)}')
print('Defining empty set s = set()')
print(f'Address of the object is id(o) {setDataType}, {id(setDataType)}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'''{Color.BOLD}Data type 'frozenset': 
            order is not preserved , 
            duplicate objects not allowed, 
            hetrogenous objects[10, 'list', True],
            immutable,
            indexing/slicing not applicable{Color.END}''')
print(f'{Color.BOLD}==================================={Color.END}')
frozenSetDataType = frozenset(setDataType)
print(f'Type of object is type(o) {frozenSetDataType}, {type(frozenSetDataType)}')
print('Defining frozen set s = frozenset(set)')
print(f'Address of the object is id(o) {setDataType}, {id(setDataType)}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'''{Color.BOLD}Data type 'dict': 
            key-value pair,
            duplicate keys not allowed, old value is replaced with new value,
            order not preserved,
            hetrogenous objects,
            mutable,
            indexing/slicing not applicable{Color.END}''')
print(f'{Color.BOLD}==================================={Color.END}')
dic = {}
dic[100] = 'Prasad'
dic[200] = 'Ramya'
dic[300] = 'Prayan'
print(f'Type of object is type(o) {dic}, {type(dic)}')
print(dic)
print(f'{Color.BOLD}==================================={Color.END}')
print(f'''{Color.BOLD}Data type 'range':
            sequence of numbers,
            order preserved,
            indexing/slicing applicable,
            immutable,
            range(n) = 0 to n-1, r = range(10) 0 to 9
            range(begin, end) = begin to end-1, r = range(1, 10) 1 to 9
            range(begin, end, increment/decrement), r = range(1, 21, 1){Color.END}''')
print(f'{Color.BOLD}==================================={Color.END}')
r = range(1, 21, 2)
print(f'Type of object is type(o) {r}, {type(r)}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'''{Color.BOLD}Data type 'bytes':
            b = bytes(10, 20),
            range must be from 0 to 255,
            indexing/slicing applicable,
            immutable{Color.END}''')
print(f'{Color.BOLD}==================================={Color.END}')
b = bytes(10)
print(f'Type of object is type(o) {b}, {type(b)}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'''{Color.BOLD}Data type 'bytearray': 
            b = bytearray(10),
            range must be from 0 to 255,
            indexing/slicing applicable,
            mutable{Color.END}''')
print(f'{Color.BOLD}==================================={Color.END}')
l = [10, 20, 30]
ba = bytearray(l)
print(f'Type of object is type(o) {ba}, {type(ba)}')
print(ba[0])
print('                                                                         ')
print('                                                                         ')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'{Color.BOLD}Precedence{Color.END}')
print(f'{Color.BOLD}==================================={Color.END}')
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
print(f'{Color.BOLD}Example:{Color.END}')
print(f'(3 + 3) * 2 ** 3 - 3 + 10 is {(3 + 3) * 2 ** 3 - 3 + 10}')
print('                                                                         ')
print('                                                                         ')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'{Color.BOLD}Conditional \'if\' Statement{Color.END}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'''{Color.BOLD}if type(itemName) is int:
    print('Type is Integer')
elif type(itemName) is str:
    print('Type is String.')
else:
    print('Couldn\'t find type'){Color.END}''')
print('                                                                         ')
print('                                                                         ')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'{Color.BOLD}Conditional \'while\' Statement{Color.END}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'''{Color.BOLD}while condition:
    print('While loop')
else:
    print('In while else') {Color.END}''')
print('                                                                         ')
print('                                                                         ')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'{Color.BOLD}\'for\' loop{Color.END}')
print(f'{Color.BOLD}==================================={Color.END}')
print(f'''{Color.BOLD}for x in 'Python':
    print(x){Color.END}''')
print(f'''{Color.BOLD}for x in ['List', 10, True]:
    print(x){Color.END}''')
print(f'''{Color.BOLD}for x in range():
    print(x){Color.END}''')
print('                                                                         ')
print('                                                                         ')
