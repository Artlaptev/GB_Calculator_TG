import re


def write_line(a):
    print(a)


def in_txt(a):
    return input(a)


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def in_comp(a):
    i = 0
    while i == 0:
        inp_data = in_txt(a)
        comp_reg = re.fullmatch(r'\d+|[+-]*\s*\d+\s*[+-]\s*\d+[i]|[+-]*\s*\d+[i]\s*[+-]\s*\d+', inp_data)
        try:
            if not comp_reg:
                raise OwnError("Неверно записано комплексное число")
        except OwnError as err:
            write_line(err)
        else:
            return inp_data


def in_int(a):
    i = 0
    while i == 0:
        inp_data = in_txt(a)
        try:
            inp_data = int(inp_data)
            if inp_data < 0:
                raise OwnError("Вы ввели отрицательное число!")
        except ValueError:
            write_line("Вы ввели не число")
        except OwnError as err:
            write_line(err)
        else:
            return inp_data


def in_act():
    act_list = ['-', '+', '*', '/']
    act = in_txt("Выберите действие: '+', '-', '*', '/': ")
    while act not in act_list:
        act = in_txt("Выберите действие: '+', '-', '*', '/': ")
    return act
