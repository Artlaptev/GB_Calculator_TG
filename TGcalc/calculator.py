# Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования.

from draw_board import draw_board
from integer import integer
from calc_fraction import calc_fraction
from my_ui import write_line, in_txt, in_int, in_act, in_comp
from complex_num import complex_num
from logs_file import logs_file

def simple_calc():
    draw_board()
    while True:
        write_line("Выберите числовое множество для ввода: целое число 'I', рациональное 'R' или комплексное 'C'")
        set_sel = in_txt("> ").upper()
        if set_sel == "I":
            write_line("Приступим к вычислению челых чисел!")
            num1 = int(in_int("x: "))
            act = in_act()
            num2 = int(in_int("y: "))
            integer(act, num1, num2)
            with open("logs_file.txt", "a", encoding="utf-8") as f:
                f.write(f"целое число {str(integer(act, num1, num2))}\n")
        elif set_sel == "R":
            write_line("Приступим к вычислению рациональных чисел!")
            a = int(in_int("Делитель_1: "))
            b = int(in_int("Делимое_1: "))
            act = in_act()
            c = int(in_int("Делитель_2: "))
            d = int(in_int("Делимое_2: "))
            calc_fraction(act, a, b, c, d)
            with open("logs_file.txt", "a", encoding="utf-8") as f:
                f.write(f"рациональное число {str(calc_fraction(act, a, b, c, d))}\n")
        elif set_sel == "C":
            write_line("Приступим к вычислению комлексных чисел!")
            comp_first = in_comp('Введите первое комплексное число: ')
            comp_act = in_act()
            comp_two = in_comp('Введите второе комплексное число: ')
            write_line(complex_num(comp_first, comp_two, comp_act))
            with open("logs_file.txt", "a", encoding="utf-8") as f:
                f.write(f"комплексное число {str(complex_num(comp_first, comp_two, comp_act))}\n")
        else:
            write_line("Жмакай 'I' или 'R' или 'C'")
        while True:
            f = in_txt('ещё раз?\n')
            if f == 'y':
                simple_calc()
            elif f == 'n':
                write_line("Chao!")
                exit()
            else:
                write_line("Выберите "'y'" или "'n'"")


simple_calc()
