field = [[" "] * 3 for i in range(3)]


def show_field():
    print('Добро пожаловать в игру крестики-нолики')
    print("      0   1   2   ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print(" ")
    print()


def input_cords():
    while True:
        cords = input("х - номер строки и у -номер столбца: ").split()

        if len(cords) != 2:
            print(" Введите две координаты! ")
            continue
        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа от 0 до 2 ")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for i in win_cord:
        symbols = []
        for a in i:
            symbols.append(field[a[0]][a[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл крестик")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл нолик")
            return True
    return False


count = 0


while True:
    count += 1
    show_field()
    if count % 2 == 1:
        print("Введите координаты для крестика: ")
    else:
        print("Введите координаты для нолика: ")

    x, y = input_cords()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if count == 9:
        print(" Ничья!")
        break
