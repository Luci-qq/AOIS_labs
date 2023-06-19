from nanologic import *

if __name__ == '__main__':
    vector_Xout4 = [[1], [0], [1], [0], [1], [0], [1], [0], [1], [0], [0], [0], [0], [0], [0], [0]]
    vector_Xout3 = [[0], [1], [1], [0], [0], [0], [0], [1], [1], [0], [0], [0], [0], [0], [0], [0]]
    vector_Xout2 = [[1], [1], [1], [0], [0], [0], [0], [0], [0], [1], [0], [0], [0], [0], [0], [0]]
    vector_Xout1 = [[0], [0], [0], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
    custom_operands = ['X1', 'X2', 'X3', 'X4']
    print('-' * 100)
    print('PDNF minimization', minimize_PDNF(vector_Xout1, custom_operands))
    print('-' * 100)
    print('PDNF minimization', minimize_PDNF(vector_Xout2, custom_operands))
    print('-' * 100)
    print('PDNF minimization', minimize_PDNF(vector_Xout3, custom_operands))
    print('-' * 100)
    print('PDNF minimization', minimize_PDNF(vector_Xout4, custom_operands))
    print('-' * 100)

    vector_X3 = [[0], [1], [1], [0], [1], [0], [0], [1]]
    vector_Dnext = [[0], [0], [0], [1], [0], [1], [1], [1]]

    custom_operands = ['X1', 'X2', 'Dprev']
    print('-' * 100)
    print('PDNF', build_PDNF(vector_X3, custom_operands))
    print('PDNF minimization', minimize_PDNF(vector_X3, custom_operands))
    print('-' * 100)
    print('PDNF', build_PDNF(vector_Dnext, custom_operands))
    print('PDNF minimization', minimize_PDNF(vector_Dnext, custom_operands))
    print('-' * 100)