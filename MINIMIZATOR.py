
from nanologic import *


if __name__ == '__main__':
    h3 = [[0], [0], [0], [0], [0], [0], [0], [1], [0], [0], [0], [0], [0], [0], [0], [1]]
    h2 = [[0], [0], [0], [1], [0], [0], [0], [1], [0], [0], [0], [1], [0], [0], [0], [1]]
    h1 = [[0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [1]]
    custom_operands = ['q3', 'q2', 'q1', 'V']

    print('-' * 100)
    print('PDNF minimization [h1]', minimize_PDNF(h1, custom_operands))
    print('-' * 100)
    print('PDNF minimization [h2]', minimize_PDNF(h2, custom_operands))
    print('-' * 100)
    print('PDNF minimization [h3]', minimize_PDNF(h3, custom_operands))
    print('-' * 100)
