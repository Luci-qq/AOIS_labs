import random
import os

os.system("chcp 1251")
os.system("cls")

class Memory:
    def __init__(self, size):
        self.memory = [format(random.randint(0, 65535), '016b') for _ in range(size)]

    def find_closest_upper_binary(self, number):
        number = format(number, '016b')
        result = min((m for m in self.memory if m >= number), default='1' * 16)
        return result

    def find_closest_lower_binary(self, number):
        number = format(number, '016b')
        result = max((m for m in self.memory if m <= number), default='0' * 16)
        return result

    def find_most_similar_binary(self, number):
        binaryNumber = format(number, '016b')
        closestBinary = max(self.memory, key=lambda x: sum(a == b for a, b in zip(x, binaryNumber)))
        return closestBinary

    def print_matrix(self):
        for m in self.memory:
            print(' '.join(m))

if __name__ == '__main__':
    res = Memory(16) #Память с 16 случайными числами
    
    print('Matrix:')
    res.print_matrix()

    print('-' * 100)

    enter1 = 8000
    result1 = res.find_closest_upper_binary(enter1)
    print(f'Ввод для поиска по ближайшему сверху: {enter1} или {format(enter1, "016b")}')
    print(f'Результат поиска по ближайшему сверху: {result1} или {int(result1, 2)}')

    print('-'*100)

    enter2 = 8000
    result2 = res.find_closest_lower_binary(enter2)
    print(f'Ввод для поиска по ближайшему снизу: {enter2} или {format(enter2, "016b")}')
    print(f'Результат поиска по ближайшему снизу: {result2} или {int(result2, 2)}')

    print('-' * 100)

    enter3 = 15000
    result3 = res.find_most_similar_binary(enter3)
    print(f'Ввод для поиска по соответствию: {enter3} или {format(enter3, "016b")}')
    print(f'Результат поиска по соответствию: {result3} или {int(result3, 2)}')

    