from Converting_logical_functions import Converting_logical_functions

a = [False, False, False, False, True, True, True, True]
b = [False, False, True, True, False, False, True, True]
c = [False, True, False, True, False, True, False, True]
dict = ['q', 'w', 'e', 'z', 'x', 'c']
length = 6

def gluing(original):
    result = []
    part_of_result = []
    for i in range(len(original)):
        for j in range(i + 1, len(original)):
            part_of_result.clear()
            fits = 0
            if original[i][0] == original[j][0]:
                fits += 1
                part_of_result.append(original[j][0])
            if original[i][1] == original[j][1]:
                fits += 1
                part_of_result.append(original[j][1])
            if original[i][2] == original[j][2]:
                fits += 1
                part_of_result.append(original[j][2])
            if fits == 2:
                result.append(part_of_result.copy())
    if not result:
        for i in range(len(original)):
            result.append(original[i])
    return result

def get_position(symbol):
    for i in range(length):
        if symbol == dict[i]:
            return i
    return -1

def int_check(number, met):
    for i in range(len(met)):
        if number == met[i]:
            return True
    return False

def gluing_sec_stage(original):
    result = []
    part_of_result = []
    met = []
    for i in range(len(original)):
        fits = False
        if int_check(i, met):
            continue
        for j in range(i + 1, len(original)):
            if original[i][0] == original[j][0]:
                if abs(get_position(original[i][1]) - get_position(original[j][1])) == 3:
                    part_of_result.append(original[j][0])
                    result.append(part_of_result.copy())
                    part_of_result.clear()
                    fits = True
                    met.append(j)
            if original[i][0] == original[j][1]:
                if abs(get_position(original[i][1]) - get_position(original[j][0])) == 3:
                    part_of_result.append(original[j][1])
                    result.append(part_of_result.copy())
                    part_of_result.clear()
                    fits = True
                    met.append(j)
            if original[i][1] == original[j][0]:
                if abs(get_position(original[i][0]) - get_position(original[j][1])) == 3:
                    part_of_result.append(original[j][0])
                    result.append(part_of_result.copy())
                    part_of_result.clear()
                    fits = True
                    met.append(j)
            if original[i][1] == original[j][1]:
                if abs(get_position(original[i][0]) - get_position(original[j][0])) == 3:
                    part_of_result.append(original[j][1])
                    result.append(part_of_result.copy())
                    part_of_result.clear()
                    fits = True
                    met.append(j)
        if not fits:
            result.append(original[i])
    return result

def repeat_check(original):
    i = 0
    while i < len(original):
        j = i + 1
        while j < len(original):
            if original[i] == original[j]:
                original.pop(j)
            else:
                j += 1
        i += 1
    return original

def extra_check(original, extra):
    i = 0
    while i < len(original):
        j = 0
        while j < len(extra):
            if original[i] == extra[j]:
                original.pop(i)
                i -= 1
                break
            j += 1
        i += 1
    return original

def gluing_third_stage(original):
    result, extra = [], []
    for i in range(len(original)):
        part_of_result = []
        if len(original[i]) > 1:
            for j in range(len(original)):
                if len(original[j]) == 1:
                    if abs(get_position(original[i][0]) - get_position(original[j][0])) == 3:
                        extra.append(original[i])
                        part_of_result.append(original[i][1])
                    elif abs(get_position(original[i][1]) - get_position(original[j][0])) == 3:
                        extra.append(original[i])
                        part_of_result.append(original[i][0])
                    else:
                        part_of_result.append(original[i][0])
                        part_of_result.append(original[i][1])
            result.append(part_of_result.copy())
        else:
            part_of_result.append(original[i][0])
            result.append(part_of_result.copy())
    result = extra_check(result, extra)
    if not result[0]:
        result.clear()
        for i in range(len(original)):
            result.append(original[i])
    return result

def print_dnf(original):
    res = ""
    for i in range(len(original)):
        for j in range(len(original[i])):
            addition = ""
            if original[i][j] == dict[0]:
                addition = "a"
            if original[i][j] == dict[1]:
                addition = "b"
            if original[i][j] == dict[2]:
                addition = "c"
            if original[i][j] == dict[3]:
                addition = "!a"
            if original[i][j] == dict[4]:
                addition = "!b"
            if original[i][j] == dict[5]:
                addition = "!c"
            res += addition
            if j != len(original[i]) - 1:
                res += "*"
        if i != len(original) - 1:
            res += " + "
    print(res)

def print_knf(original):
    res = ""
    for i in range(len(original)):
        for j in range(len(original[i])):
            addition = ""
            if j == 0:
                res += "("
            if original[i][j] == dict[0]:
                addition = "a"
            if original[i][j] == dict[1]:
                addition = "b"
            if original[i][j] == dict[2]:
                addition = "c"
            if original[i][j] == dict[3]:
                addition = "!a"
            if original[i][j] == dict[4]:
                addition = "!b"
            if original[i][j] == dict[5]:
                addition = "!c"
            res += addition
            if j != len(original[i]) - 1:
                res += "+"
            else:
                res += ")"
        if i != len(original) - 1:
            res += "*"
    print(res)

def print_kf(original):
    res = ''
    for i in range(len(original)):
        addition = ''
        if original[i] == dict[0]:
            addition = 'a'
        elif original[i] == dict[1]:
            addition = 'b'
        elif original[i] == dict[2]:
            addition = 'c'
        elif original[i] == dict[3]:
            addition = '!a'
        elif original[i] == dict[4]:
            addition = '!b'
        elif original[i] == dict[5]:
            addition = '!c'
        res += addition
        if i != len(original) - 1:
            res += '+'
    print(res)

def print_df(original):
    res = ""
    for i in range(len(original)):
        addition = ""
        if original[i] == dict[0]:
            addition = "a"
        elif original[i] == dict[1]:
            addition = "b"
        elif original[i] == dict[2]:
            addition = "c"
        elif original[i] == dict[3]:
            addition = "!a"
        elif original[i] == dict[4]:
            addition = "!b"
        elif original[i] == dict[5]:
            addition = "!c"
        res += addition
        if i != len(original) - 1:
            res += "*"
    print(res)

def log_formula_parse(formula):
    result_literal = True
    part_of_result = []
    segment = []
    if formula[0] == '(':
        result_literal=False
    i = 0
    while i < len(formula):
        if i != 0 and formula[i - 1] == '!':
            i += 1
            continue
        if formula[i] == 'a':
            segment.append(dict[0])
        elif formula[i] == 'b':
            segment.append(dict[1])
        elif formula[i] == 'c':
            segment.append(dict[2])
        elif formula[i] == '!':
            if formula[i+1] == 'a':
                segment.append(dict[3])
            elif formula[i+1] == 'b':
                segment.append(dict[4])
            elif formula[i+1] == 'c':
                segment.append(dict[5])
            i += 1
        elif formula[i] == '+' and result_literal==True:
            part_of_result.append(segment)
            segment = []
        elif formula[i] == '*' and result_literal==False:
            part_of_result.append(segment)
            segment = []
        i += 1
    
    part_of_result.append(segment)
    result = (part_of_result, result_literal)
    return result

def find_excess(expression, res):
    excess = []
    matches = []
    timer = [0] * len(expression)
    
    for i in range(len(res)):
        intersectionString = []
        for j in range(len(expression)):
            times = 0
            for k in range(len(res[i])):
                if res[i][k] in expression[j]:
                    times += 1
            if times == len(res[i]):
                intersectionString.append(j)
                timer[j] += 1
        matches.append(intersectionString)
    
    for i in range(len(matches)):
        times = 0
        for k in range(len(matches[i])):
            if timer[matches[i][k]] >= 2:
                times += 1
        if times == len(matches[i]):
            excess.append(res[i])
    
    return (excess, matches)

def calculate_tab(form, intermediate, matches, type):
    res = []
    if type:
        print_dnf(form)
    else:
        print_knf(form)
    for i in range(len(intermediate)):
        if type:
            print("  ")
        else:
            print("   ")
        for j in range(len(form)):
            for k in range(len(matches[1][i])):
                if matches[1][i][k] == j:
                    print("X", end="")
                else:
                    print(" ", end="")
            print("       ", end="")
        if type:
            print_df(intermediate[i])
        else:
            print_kf(intermediate[i])
    print("\nResult: ")
    res = extra_check(intermediate, matches[0])
    if type:
        print_dnf(res)
    else:
        print_knf(res)

def carno_method(function, type):
    Carno = []
    firstString = []
    secondString = []
    firstString.append(function[0])
    firstString.append(function[1])
    firstString.append(function[3])
    firstString.append(function[2])
    secondString.append(function[4])
    secondString.append(function[5])
    secondString.append(function[7])
    secondString.append(function[6])
    Carno.append(firstString)
    Carno.append(secondString)
    return Carno

def out_table_method(carno, type):
    print("a/bc | 00 | 01 | 11 | 10 |\n")
    for i in range(len(carno)):
        if i == 0:
            print("  0  | ", end="")
        else:
            print("  1  | ", end="")
        for j in range(len(carno[i])):
            print(int(carno[i][j]), end="")
            if j != len(carno[i]) - 1:
                print("  | ", end="")
        print("\n")


