from math import *

def fig(arg1):
    s = 4 * pi * (arg1 ** 2)
    return s

def main():
    n = int(input("Выберите, площадь какой фигуры вы хотите узнать?\n 1-куб\n 2-параллелепипед\n 3-цилиндр\n 4-шар\n n = "))

    if n == 1:
        a = float(input("Введите радиус шара = "))
        print("Площадь шара с радиусом = ", a, "равна 4πR² ", fig1(a))

if __name__ == '__main__':
    main()
