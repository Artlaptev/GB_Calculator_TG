def complex_num(comp_first, comp_two, comp_act):
    class ComplexNumb:
        def __init__(self, complex):
            self.complex = complex
            complex = (((complex.replace('+', '/+')).replace('-', '/-')).strip()).strip('/')
            complex_lst = (''.join(complex.split())).split('/')
            self.complex_lst = complex_lst
            self.complex_b = '0i'
            self.complex_a = '0'
            if len(complex_lst) == 1:
                if 'i' in complex_lst[0]:
                    self.complex_b = complex_lst[0]
                else:
                    self.complex_a = complex_lst[0]
            if len(complex_lst) == 2:
                if 'i' in complex_lst[0]:
                    self.complex_a = complex_lst[1]
                    self.complex_b = complex_lst[0]
                else:
                    self.complex_a = complex_lst[0]
                    self.complex_b = complex_lst[1]

        def __add__(self, other):
            complex_new_a = int(self.complex_a) + int(other.complex_a)
            complex_new_b = str(int(self.complex_b.replace('i', '')) + int((other.complex_b).replace('i', ''))) + 'i'
            if '-' in complex_new_b:
                return ComplexNumb((str(complex_new_a) + str(complex_new_b)))
            else:
                return ComplexNumb((str(complex_new_a) + '+' + str(complex_new_b)))

        def __sub__(self, other):
            complex_new_a = int(self.complex_a) - int(other.complex_a)
            complex_new_b = str(int(self.complex_b.replace('i', '')) - int((other.complex_b).replace('i', ''))) + 'i'
            if '-' in complex_new_b:
                return ComplexNumb((str(complex_new_a) + str(complex_new_b)))
            else:
                return ComplexNumb((str(complex_new_a) + '+' + str(complex_new_b)))

        def __truediv__(self, other):
            a = int(self.complex_a)
            b = int(self.complex_b.replace('i', ""))
            c = int(other.complex_a)
            d = int(other.complex_b.replace('i', ""))
            complex_new_a = round((a * c + b * d) / (c ** 2 + d ** 2), 3)
            complex_new_b_1 = round((b * c - a * d) / (c ** 2 + d ** 2), 3)
            complex_new_b = str(complex_new_b_1) + 'i'
            if '-' in complex_new_b:
                return ComplexNumb((str(complex_new_a) + str(complex_new_b)))
            else:
                return ComplexNumb((str(complex_new_a) + '+' + str(complex_new_b)))

        def __mul__(self, other):
            complex_new_a = int(self.complex_a) * int(other.complex_a)
            complex_new_b = str(int(self.complex_a.replace('i', '')) * int((other.complex_b).replace('i', '')) + \
                                int(self.complex_b.replace('i', '')) * int((other.complex_a).replace('i', '')) - \
                                int(self.complex_b.replace('i', '')) * int((other.complex_a).replace('i', ''))) + 'i'
            if '-' in complex_new_b:
                return ComplexNumb((str(complex_new_a).replace('/', '') + str(complex_new_b.replace('/', ''))))
            else:
                return ComplexNumb((str(complex_new_a).replace('/', '') + '+' + str(complex_new_b.replace('/', ''))))

    a = ComplexNumb(comp_first)
    b = ComplexNumb(comp_two)

    if comp_act == '+':
        t = a + b
        return t.complex
    elif comp_act == '*':
        return (a * b).complex
    elif comp_act == '-':
        return (a - b).complex
    elif comp_act == '/':
        return (a / b).complex
