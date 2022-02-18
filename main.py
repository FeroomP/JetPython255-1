from math import *

def fig3(arg1, arg2):
    s = 2*pi*arg1*arg2+2*pi*arg1*arg1
    return s

def Ob3(arg1, arg2):
    v = 2*pi*arg1*arg1*arg2
    return v

def main():
    n = int(input("Выберите, площадь какой фигуры вы хотите узнать?\n 1-куб\n 2-параллелепипед\n 3-цилиндр\n 4-шар\n n = "))

    if n == 3:
        r = float(input("введите радиус окружности основания цилиндра r="))
        h = float(input("введите высоту цилиндра h="))
        print("объём цилиндра с радиусом r=", r, "и высотой h=", h, "равна", Ob3(r, h))
        print("площадь поверхности цилиндра с радиусом r=", r, "и высотой h=", h, "равна", fig3(r, h))

if __name__ == '__main__':
    main()
