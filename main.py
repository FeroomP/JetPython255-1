from math import *

def fig4(arg1):
    s = 4 * pi * (arg1 ** 2)
    return s

def fig3(arg1, arg2):
    v = 2*pi*arg1*arg1*arg2
    return v

def main():
    n = int(input("Выберите, площадь какой фигуры вы хотите узнать?\n 1-куб\n 2-параллелепипед\n 3-цилиндр\n 4-шар\n n = "))

    if n == 4:
        a = float(input("Введите радиус шара = "))
        print("Площадь шара с радиусом = ", a, "равна 4πR² ", fig4(a))

    if n == 3:
        r = float(input("введите радиус окружности основания цилиндра r="))
        h = float(input("введите высоту цилиндра h="))
        print("объём цилиндра с радиусом r=", r, "и высотой h=", h, "равна", fig3(r, h))

if __name__ == '__main__':
    main()
