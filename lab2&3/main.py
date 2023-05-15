from Converting_logical_functions import Converting_logical_functions
import os
from lab3 import *
##Test formulas
#(a*b)+(!a*(c+b))
#!((a+c)*(!(b*c)))

def clear_console():
     os.system('clear')
     os.system('cls')


if __name__ == '__main__':
     formula = input("Formula:")
     sv = Converting_logical_functions(formula)
     print("\n",sv)
     formula = input()
     clf = Converting_logical_functions(formula)
     function = clf.get_log_function(formula)
     print("1) - SDNF\n2) - SKNF\n")
     form_print=""
     choice = int(input())
     if choice == 1:
          form = clf.get_log_sdnf()
          form_print = "Sdnf: "
     else:
          form = clf.get_log_sknf()
          form_print="Sknf: "     
     clear_console()
     form_print+=form
     print(f"Inputed formula: {formula}\n{form_print}")
     expression = log_formula_parse(form)
     intermediate = gluing(expression[0])
     print("\nCalculating:\n1:")
     if expression[1]:
          print_dnf(intermediate)
     else:
          print_knf(intermediate)
     intermediate = gluing_sec_stage(intermediate)
     intermediate = repeat_check(intermediate)
     print("2:")
     if expression[1]:
          print_dnf(intermediate)
     else:
          print_knf(intermediate)
     res = gluing_third_stage(intermediate)
     res = repeat_check(res)
     intermediate = res.copy()
     print("3:")
     if expression[1]:
          print_dnf(res)
     else:
          print_knf(res)
     print("Result:\n", end="")
     extra = find_excess(expression[0], res.copy())
     res = extra_check(res.copy(), extra[0])
     if expression[1]:
          print_dnf(res.copy())
     else:
          print_knf(res.copy())
     print("\nTabular-calculating:\n")
     calculate_tab(expression[0], intermediate, extra, expression[1])
     print("\nTabular:\n")
     out_table_method(carno_method(function, expression[1]), expression[1])
     print("Result:\n", end="")
     if expression[1]:
          print_dnf(res)
     else:
          print_knf(res)