import os
import math
from math import pow

#Constants
BITS_NUM=8
BINARY_ZERO=[0,0,0,0,0,0,0,0]
BINARY_ONE=[0,0,0,0,0,0,0,1]
BINARY_MINUS_ONE_COMPLEMENTARY = [1, 1, 1, 1, 1, 1, 1, 1]
FRACTIONAL_BITS_NUM = 23
PERCEPTION = 127


class Binary_float:
    def __init__(self):
        self.mantissa = []
        self.exponent = BINARY_ZERO.copy()
        self.sign = False
    def __str__(self) -> str:
        result=""
        result+=str(self.sign)+" "
        for bit in self.exponent:
            result+=str(round(bit))
        result+=" "
        for bit in self.mantissa:
            result+=str(round(bit))
        return result
        


def convert_decimal_to_straight_binary(value):
    result_binary=[]
    if value==0:
        result_binary=BINARY_ZERO.copy()
        return result_binary
    value_ = abs(value)
    while value_:
        result_binary.insert(0,value_ % 2)
        value_ //=2
    for bit in range(BITS_NUM - len(result_binary)):
        result_binary.insert(0,0)
    if value < 0:
        result_binary[0]=1
    return result_binary

def convert_decimal_to_inverse_binary(value):
    result_binary=convert_decimal_to_straight_binary(value)
    if value >= 0:
        return result_binary
    else: 
        for bit_index in range(1,len(result_binary)):
            if result_binary[bit_index]==1:
                result_binary[bit_index]=0
            else:
                result_binary[bit_index]=1
    return result_binary

def convert_decimal_to_complementary_binary(value):
        result_binary=convert_decimal_to_inverse_binary(value)
        result_binary=addition_binary(result_binary,BINARY_ONE.copy())
        return result_binary

def convert_straight_to_complementary_binary(value):
    for bit_index in range(len(value)):
        if value[bit_index]==1:
            value[bit_index]=0
        else:
            value[bit_index]=1
    value[0]=1
    value=addition_binary(value,BINARY_ONE.copy())
    return value

def convert_inverse_to_straight(value):
    if(value[0]==1):
        for bit_index in range(len(value)):
            if value[bit_index]==1:
                value[bit_index]=0
            else:
                value[bit_index]=1
            value[0]=1
            return value
    else:
        return value
    

def addition_binary(value1,value2):
    result_binary = []
    overflow = False
    for bit_index in range(len(value1)-1, -1, -1):
        if value1[bit_index] == 0 and value2[bit_index] == 0 and not overflow:
            result_binary.insert(0, 0)
            overflow = False
        elif value1[bit_index] == 0 and value2[bit_index] == 0 and overflow:
            result_binary.insert(0, 1)
            overflow = False
        elif value1[bit_index] == 1 and value2[bit_index] == 0 and not overflow:
            result_binary.insert(0, 1)
            overflow = False
        elif value1[bit_index] == 1 and value2[bit_index] == 0 and overflow:
            result_binary.insert(0, 0)
            overflow = True
        elif value1[bit_index] == 0 and value2[bit_index] == 1 and not overflow:
            result_binary.insert(0, 1)
            overflow = False
        elif value1[bit_index] == 0 and value2[bit_index] == 1 and overflow:
            result_binary.insert(0, 0)
            overflow = True
        elif value1[bit_index] == 1 and value2[bit_index] == 1 and not overflow:
            result_binary.insert(0, 0)
            overflow = True
        elif value1[bit_index] == 1 and value2[bit_index] == 1 and overflow:
            result_binary.insert(0, 1)
            overflow = True
    return result_binary

def multiply_binary(value1, value2):
    minus_one_complementary = convert_decimal_to_complementary_binary(-1)
    result_binary = BINARY_ZERO.copy()
    flag = False
    if value1[0] == value2[0]:
        flag = True
    if value2[0] == 1:
        value2[0] = 0
    while value2 != BINARY_ZERO.copy():
        result_binary = addition_binary(value1, result_binary)
        value2 = addition_binary(value2, minus_one_complementary)
    if flag:
        result_binary[0]=0
    else:
        result_binary[0]=1
    return result_binary

def division_binary(value1,value2):
    result_binary, remainder, temp_remainder = [],[],[]
    times = 0
    sign = False
    if value1[0] == value2[0]:
        sign = True
    value1[0] = 0
    value2[0] = 1
    value2 = convert_straight_to_complementary_binary(value2)
    while True:
        temp_remainder = addition_binary(value1, value2)
        if temp_remainder[0] == 1:
            break
        else:
            times += 1
        value1 = addition_binary(value1, value2)
    for i in range(5):
        value1.append(0)
        del value1[0]
        temp_remainder = addition_binary(value1, value2)
        if temp_remainder[0] == 1:
            remainder.append(0)
            continue
        else:
            remainder.append(1)
        value1 = addition_binary(value1, value2)
    result_binary = convert_decimal_to_straight_binary(times)
    if not sign:
        result_binary[0] = 1
    result_binary=[str(_) for _ in result_binary ]
    result_binary+='.'
    remainder=[str(_) for _ in remainder]
    result_binary+=remainder
    return result_binary

def pretty_output(value):
    line=''
    for item in value:
        line+=str(item)
    print(line)

def convert_float_to_binary_util(value):
    fractional,integer=math.modf(value)
    fractional_bin = []
    integer_bin = convert_decimal_to_straight_binary(integer)
    if integer == 0:
        integer_bin = BINARY_ZERO.copy()
    counter = -1
    while fractional > 0:
        if fractional - pow(2, counter) >= 0:
            fractional_bin.append(1)
            fractional -= pow(2, counter)
        else:
            fractional_bin.append(0)
        counter -= 1
    result = []
    result.append(integer_bin)
    result.append(fractional_bin)
    return result

def convert_float_to_binary(value):
    res = Binary_float()
    res.sign = 0
    if value < 0:
        res.sign = 1
    binary_value = convert_float_to_binary_util(value)
    integer_bin = binary_value[0]
    fractional_bin = binary_value[1]
    if integer_bin == BINARY_ZERO.copy():
        while integer_bin != BINARY_ONE.copy():
            integer_bin.append(fractional_bin[0])
            del integer_bin[0]
            del fractional_bin[0]
            fractional_bin.append(0)
            res.exponent = addition_binary(res.exponent, BINARY_MINUS_ONE_COMPLEMENTARY.copy())
    while integer_bin != BINARY_ONE.copy():
        fractional_bin.insert(0, integer_bin[len(integer_bin) - 1])
        integer_bin.pop()
        integer_bin.insert(0, 0)
        res.exponent = addition_binary(res.exponent, BINARY_ONE.copy())
    res.exponent = addition_binary(res.exponent, convert_decimal_to_straight_binary(PERCEPTION))
    for i in range(BITS_NUM - len(res.exponent)):
        res.exponent.insert(0, 0)
    res.mantissa = fractional_bin
    for i in range(len(res.mantissa), FRACTIONAL_BITS_NUM):
        res.mantissa.append(0)
    return res

def lower_exponent(a, b):
    return addition_binary(a.exponent, multiply_binary(b.exponent, BINARY_MINUS_ONE_COMPLEMENTARY.copy()))[0]==1


def alignment_of_exponents(a, b):
    times = 0
    while a.exponent != b.exponent:
        a.exponent = addition_binary(a.exponent, BINARY_ONE.copy())
        if times < 1:
            a.mantissa.insert(0, 1)
        else:
            a.mantissa.insert(0, 0)
        a.mantissa.pop()
        times += 1
    if times == 0:
        a.mantissa.insert(0, 1)
    else:
        a.mantissa.insert(0, 0)
    a.exponent = addition_binary(a.exponent, BINARY_ONE.copy())
    a.mantissa.pop()
    b.mantissa.insert(0, 1)
    b.exponent = addition_binary(b.exponent, BINARY_ONE.copy())
    b.mantissa.pop()
    pair_of_terms = (a, b)
    return pair_of_terms

def addition_float_binary(a, b):
    res = Binary_float()
    if lower_exponent(a, b):
        pair_of_terms = alignment_of_exponents(a, b)
    else:
        pair_of_terms = alignment_of_exponents(b, a)
    a = pair_of_terms[0]
    b = pair_of_terms[1]
    a.mantissa.insert(0, 0)
    b.mantissa.insert(0, 0)
    res.exponent = b.exponent
    res.mantissa = addition_binary(a.mantissa, b.mantissa)
    if not res.mantissa[0]:
        res.exponent = addition_binary(res.exponent, BINARY_MINUS_ONE_COMPLEMENTARY.copy())
        res.mantissa.pop(0)
        res.mantissa.append(0)
    res.mantissa.pop(0)
    res.sign = 0
    return res

def sum_utility(value1,value2):
    value1_binary=convert_decimal_to_straight_binary(value1)
    value2_binary=convert_decimal_to_straight_binary(value2)
    if value1_binary[0]==1: value1_binary=convert_straight_to_complementary_binary(value1_binary)
    if value2_binary[0]==1: value2_binary=convert_straight_to_complementary_binary(value2_binary)    
    pretty_output(addition_binary(value1_binary,value2_binary))

def sum_float_utility(value1,value2):
    value1_binary=convert_float_to_binary(value1)
    value2_binary=convert_float_to_binary(value2)
    result_binary = addition_float_binary(value1_binary,value2_binary)
    return result_binary

def multiply_utility(value1,value2):
    value1_binary=convert_decimal_to_straight_binary(value1)
    value2_binary=convert_decimal_to_straight_binary(value2)
    pretty_output(multiply_binary(value1_binary,value2_binary))

def division_utility(value1,value2):
    value1_binary=convert_decimal_to_straight_binary(value1)
    value2_binary=convert_decimal_to_straight_binary(value2)
    pretty_output(division_binary(value1_binary,value2_binary))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def integer_binary_operations():
    clear_screen()
    print('Integer Binary Operations:')
    value1 = int(input("Enter the first integer: "))
    value2 = int(input("Enter the second integer: "))
    print("Choose an operation:")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Division")
    print("4. Escape")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        sum_utility(value1,value2)
    elif choice == 2:
        multiply_utility(value1,value2)
    elif choice == 3:
        division_utility(value1,value2)
    elif choice == 4:
        print("Escape selected. Returning to main menu.")
        main_menu()
        return
    else:
        print("Invalid choice. Please try again.")
        integer_binary_operations()
    input("Press enter to continue...")
    integer_binary_operations()

def float_binary_addition():
    clear_screen()
    print('Float Binary Addition:')
    value1 = float(input("Enter the first float: "))
    value2 = float(input("Enter the second float: "))
    print(convert_float_to_binary(value1))
    print(convert_float_to_binary(value2))
    print(sum_float_utility(value1,value2))    
    input("Press enter to continue...")
    main_menu()


def main_menu():
    clear_screen()
    print("Choose an option:")
    print("1. Integer Binary Operations")
    print("2. Float Binary Addition")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        integer_binary_operations()
    elif choice == 2:
        float_binary_addition()
    elif choice == 3:
        print("Exiting program.")
        exit()
    else:
        print("Invalid choice. Please try again.")
    input("Press enter to continue...")
    main_menu()


main_menu()