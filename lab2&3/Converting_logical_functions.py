class Converting_logical_functions:
    def __init__(self,log_formula) -> None:
        self.const_a = [0, 0, 0, 0, 1, 1, 1, 1]
        self.const_b = [0, 0, 1, 1, 0, 0, 1, 1]
        self.const_c = [0, 1, 0, 1, 0, 1, 0, 1]
        self.const_log_dict  = ['q', 'w', 'e', 'z', 'x', 'c']
        self.const_length = 6
        self.const_num_of_solutions = 8
        self.output = []
        self.log_function = self.get_log_function(log_formula)
        self.output.append(self.build_table())
        self.output.append(f"Sdnf: {self.get_log_sdnf()} \n")
        self.output.append(f"Sknf: {self.get_log_sknf()} \n")
        self.output.append(self.get_dec_sdnf())
        self.output.append(self.get_dec_sknf())
        self.output.append(self.bin_to_dec_str_utill())

    def build_table(self) -> str:
        table_result = "Truth table:\n"
        table_result += " a   b   c   |   f\n"
        table_result += "-------------------\n"
        for i in range(self.const_num_of_solutions):
            table_result += " {}   {}   {}   |   {}\n".format(int(self.const_a[i]), int(self.const_b[i]), int(self.const_c[i]), int(self.log_function[i]))
        table_result+="\n"
        return table_result

    def get_log_function(self,log_formula):
        res = 0
        reverse_notice = self.infix_to_postfix(log_formula)
        res_log_function = []
        for i in range(self.const_num_of_solutions):
            res = self.slv_log_formula(reverse_notice, self.const_a[i], self.const_b[i], self.const_c[i])
            res_log_function.append(res)
        return res_log_function
    
    def infix_to_postfix(self,str):
        stack = []
        result = []
        for c in str:
            if c == 'a' or c == 'b' or c == 'c':
                result.append(c)
            elif c == '(':
                stack.append('(')
            elif c == ')':
                while stack[-1] != '(':
                    result.append(stack[-1])
                    stack.pop()
                stack.pop()
            else:
                while stack and self.get_precedence(c) <= self.get_precedence(stack[-1]):
                    result.append(stack[-1])
                    stack.pop()
                stack.append(c)
        while stack:
            result.append(stack[-1])
            stack.pop()
        return result

    def get_precedence(self,c):
        if c == '!':
            return 3
        elif c == '*':
            return 2
        elif c == '+':
            return 1
        else:
            return -1

    def slv_log_formula(self,reverse_notice, a, b, c):
        stack = []
        for s in reverse_notice:
            if s != "+" and s != "!" and s != "*":
                if s == "a":
                    stack.append(a)
                elif s == "b":
                    stack.append(b)
                elif s == "c":
                    stack.append(c)
            else:
                if s == "+":
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y or x)
                elif s == "!":
                    x = stack.pop()
                    stack.append(not x)
                elif s == "*":
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y and x)
        return stack.pop()
    
    def get_log_sdnf(self) -> str:
        sdnf_res = ""
        for i in range(self.const_num_of_solutions):
            if self.log_function[i]:
                if self.const_a[i]:
                    sdnf_res += "a*"
                else:
                    sdnf_res += "!a*"
                if self.const_b[i]:
                    sdnf_res += "b*"
                else:
                    sdnf_res += "!b*"
                if self.const_c[i]:
                    sdnf_res += "c"
                else:
                    sdnf_res += "!c"
                sdnf_res += " + "
        sdnf_res = sdnf_res[:-3]
        return sdnf_res
        
    def get_log_sknf(self) -> str:
        sknf_res = ""
        for i in range(self.const_num_of_solutions):
            if not self.log_function[i]:
                if not self.const_a[i]:
                    sknf_res += "(a + "
                else:
                    sknf_res += "((!a) +"
                if not self.const_b[i]:
                    sknf_res += " b + "
                else:
                    sknf_res += "(!b) +"
                if not self.const_c[i]:
                    sknf_res += " c)"
                else:
                    sknf_res += "(!c))"
                sknf_res += " * "
        sknf_res = sknf_res[:-3] # remove last " * "
        return sknf_res

    def bin_to_dec(self,digit):
        result = 1
        position = 0
        while len(digit) > position:
            if digit[position] == 1:
                break
            position += 1
        if position == len(digit):
            return 0
        for i in range(position + 1, len(digit)):
            if digit[i]:
                result = result * 2 + 1
            else:
                result *= 2
        return result
    
    def bin_to_dec_str_utill(self) -> str:
        dec_res = "Index: "
        dec_res += str(self.bin_to_dec(self.log_function))
        dec_res +="\n"
        return dec_res

    def get_dec_sdnf(self) -> str:
        dec_sdnf_result = "Sdnf decimal: "
        for i in range(self.const_num_of_solutions):
            if self.log_function[i]:
                result = []
                if self.const_a[i]:
                    result.append(1)
                else:
                    result.append(0)
                if self.const_b[i]:
                    result.append(1)
                else:
                    result.append(0)
                if self.const_c[i]:
                    result.append(1)
                else:
                    result.append(0)
                dec_sdnf_result += str(self.bin_to_dec(result))
                dec_sdnf_result += " + "
        dec_sdnf_result = dec_sdnf_result[:-3]
        dec_sdnf_result+="\n"
        return dec_sdnf_result

    def get_dec_sknf(self) ->str:
        dec_sknf_res = "Sknf decimal: "
        for i in range(self.const_num_of_solutions):
            if not self.log_function[i]:
                result = []
                if self.const_a[i]:
                    result.append(1)
                else:
                    result.append(0)
                if self.const_b[i]:
                    result.append(1)
                else:
                    result.append(0)
                if self.const_c[i]:
                    result.append(1)
                else:
                    result.append(0)
                dec_sknf_res += str(self.bin_to_dec(result))
                dec_sknf_res += " * "
        dec_sknf_res = dec_sknf_res[:-3]
        dec_sknf_res+="\n"
        return dec_sknf_res
    
    def __str__(self):
        output_res = ""
        for item in self.output:
            output_res+=str(item)
        return output_res
    
