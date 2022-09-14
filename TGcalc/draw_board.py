import my_ui

def draw_board():
    my_ui.write_line("Простой калькулятор")
    board = ['7', '8', '9', '/', '4', '5', '6', '-', '1', '2', '3', '+', '*', '0', ' ', '=']
    my_ui.write_line("-" * 17)
    for i in range(0, 4):
        print("|", board[0 + i * 4], "|", board[1 + i * 4], "|", board[2 + i * 4], "|", board[3 + i * 4], "|")
        my_ui.write_line("-" * 17)