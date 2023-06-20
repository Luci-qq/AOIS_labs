import copy

class AddrMemory:
    def __init__(self, numbers):
        self.memory = []
        self.vertical_mtrx = []
        self.horisontal_mtrx = []
        for i in range(len(numbers)):
            self.memory.append(self.dec_to_bin(numbers[i]))
        print('Normal matrix:')
        self.get_mtrx(self.memory)
        self.horisontal_diag_addresation()
        self.vertical_diag_addresation ()
        self.v = '011'


    def srch_value(self, value, mtrx_type):
        value = self.dec_to_bin(value)
        result = ''
        res_counter = 0
        if mtrx_type == 'normal':
            mtrx = self.memory
            read = lambda x: x
        elif mtrx_type == 'horisontal':
            mtrx = self.horisontal_mtrx
            read = self.horisontal_read
        elif mtrx_type == 'vertical':
            mtrx = self.vertical_mtrx
            read = self.vertical_read
        for row in mtrx:
            value = read(row)
            counter = sum(1 for j in range(len(value)) if value[j] == value[j])
            if counter > res_counter:
                result = value
                res_counter = counter
        return result

    def dec_to_bin(self, value):
        result = bin(value)[2:]
        result = '0' * (16 - len(result)) + result
        return list(result)

    def get_mtrx(self, mtrx):
        for mtrx_row in mtrx:
            print(' '.join(mtrx_row))
        print('')

    def vertical_diag_addresation(self):
        self.vertical_mtrx = []
        for y in range(16):
            row = []
            for x in range(16):
                row.append(self.memory[(y - x) % 16][x])
            self.vertical_mtrx.append(row)
        print('Matrix (vertical diagonal addressation): ')
        self.get_mtrx(self.vertical_mtrx)

    def horisontal_diag_addresation(self):
        self.horisontal_mtrx = [row[y:] + row[:y] for y, row in enumerate(self.memory)]
        print('Matrix (horisontal diagonal addressation): ')
        self.get_mtrx(self.horisontal_mtrx)

    def vertical_read(self, address):
        result = []
        for x in range(len(self.memory[0])):
            y = (address + x) % 16
            result.append(self.vertical_mtrx[y][x])
        return result

    def horisontal_read(self, address):
        result = self.horisontal_mtrx[address][16-address:] + self.horisontal_mtrx[address][:16-address]
        return result

    def const_zero(self):
        print('Constant: ', end='')
        print(''.join(['0']*16))

    def const_one(self):
        print('Constant 1: ', end='')
        print(''.join(['1']*16))

    def repeat_arg(self, address, mtrx_type):
        if mtrx_type == 'normal':
            print('Repeat argument: ', end='')
            print(''.join(self.memory[address - 1]))
        elif mtrx_type == 'vertical':
            value = self.vertical_read(address)
            print('Repeat argument: ', end='')
            print(''.join(value))
        elif mtrx_type == 'horisontal':
            value = self.horisontal_read(address)
            print('Repeat argument: ', end='')
            print(''.join(value))

    def negating_arg(self, addr, mtrx_type):
        value = 0
        if mtrx_type == 'normal':
            value = self.memory[addr]
        elif mtrx_type == 'vertical':
            value = self.vertical_read(addr)
        elif mtrx_type == 'horisontal':
            value = self.horisontal_read(addr)

        for i in range(len(value)):
            if value[i] == '1':
                value[i] = '0'
            else:
                value[i] = '1'

        print('Negating argument: ', end='')
        print(''.join(value))
        
    def sum(self):
            for i in range(len(self.memory)):
                vj = []
                for j in range(3):
                    vj.append(self.memory[i][j])

                if ''.join(vj) == self.v:
                    aj = []
                    bj = []
                    sj = []
                    j = 3
                    while j < 7:
                        aj.append(self.memory[i][j])
                        j += 1
                    while j < 11:
                        bj.append(self.memory[i][j])
                        j += 1
                    carry = False
                    j = 3
                    while j >= 0:
                        if aj == '1' and bj == '0' and carry is False:
                            sj.insert(0, '1')
                            j -= 1
                        elif aj == '0' and bj == '1' and carry is False:
                            sj.insert(0, '1')
                            j -= 1
                        elif aj == '1' and bj == '1' and carry is True:
                            sj.insert(0, '1')
                            j -= 1
                        elif aj == '0' and bj == '0' and carry is True:
                            sj.insert(0, '1')
                            carry = False
                            j -= 1
                        else:
                            sj.insert(0, '0')
                            j -= 1
                    if carry:
                        sj.insert(0, '1')
                    else:
                        sj.insert(0, '0')
                    j = 11
                    result = copy.deepcopy(self.memory[i])
                    while j < 16:
                        result[j] = sj[j - 11]
                        j += 1
                    print('Sum: ', end='')
                    print(''.join(result))


if __name__ == '__main__':
    test_addr_memory = AddrMemory([255, 6212, 2341, 23421, 7593, 20, 1234, 8139, 50000, 1, 42690, 15278, 32190, 1313, 24458, 36423])
    test_value = 5
    test_addr_memory.const_zero()
    test_addr_memory.const_one()
    print('From normal matrix: ', end='')
    print(''.join(test_addr_memory.memory[test_value]))
    print(f'Read horisontal: {test_addr_memory.horisontal_read(test_value)}')
    print(f'Read vertical: {test_addr_memory.vertical_read(test_value)}')
    test_addr_memory.negating_arg(test_value, 'vertical')
    test_addr_memory.negating_arg(test_value, 'horisontal')
    test_addr_memory.repeat_arg(test_value, 'vertical')
    test_addr_memory.repeat_arg(test_value, 'horisontal')
    test_addr_memory.sum()