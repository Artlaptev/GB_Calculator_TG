from calculations import div, mult, diff, sum
from my_ui import write_line
from fractions import Fraction


def calc_fraction(act, a, b, c, d):
    if act == "+":
        return sum(Fraction(a, b), Fraction(c, d))
    elif act == "-":
        return diff(Fraction(a, b), Fraction(c, d))
    elif act == "*":
        return mult(Fraction(a, b), Fraction(c, d))
    elif act == "/":
        return div(Fraction(a, b), Fraction(c, d))