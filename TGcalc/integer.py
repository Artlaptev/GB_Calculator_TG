from calculations import div, mult, diff, sum
from my_ui import write_line


def integer(act, num1, num2):
    if act == "+":
        return sum(num1, num2)
    elif act == "-":
        return diff(num1, num2)
    elif act == "*":
        return mult(num1, num2)
    elif act == "/":
        if num2 == 0:
            return "∞"
        elif num2 == 0 and num1 == 0:
            return "nan"
        else:
            return div(num1, num2)