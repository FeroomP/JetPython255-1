from math import *

def fig3(arg1, arg2):
    s = 2*pi*arg1*arg2+2*pi*arg1*arg1
    return s

def Ob3(arg1, arg2):
    v = 2*pi*arg1*arg1*arg2
    return v

def ob3(arg1, arg2):
    v = 2*pi*arg1*arg1*arg2
    return v

def fig4(arg1):
    s = 4 * pi * (arg1 ** 2)
    return s

def ob4(arg1):
    v = 4 / 3 * pi * (arg1 ** 3)
    return s

def main():

  n = int(input("Выберите, площадь поверхности и объём какой фигуры вы хотите узнать?\n 1-куб\n 2-параллелепипед\n 3-цилиндр\n 4-шар\n n = "))
  
      if n == 3:
        r = float(input("введите радиус окружности основания цилиндра r="))
        h = float(input("введите высоту цилиндра h="))
        print("объём цилиндра с радиусом r=", r, "и высотой h=", h, "равна", Ob3(r, h))
        print("площадь поверхности цилиндра с радиусом r=", r, "и высотой h=", h, "равна", fig3(r, h))

    if n == 3:
        r = float(input("введите радиус окружности основания цилиндра r="))
        h = float(input("введите высоту цилиндра h="))
        print("объём цилиндра с радиусом r=", r, "и высотой h=", h, "равна", fig3(r, h))
        
    if n == 4:
        a = float(input("Введите радиус шара = "))
        print("Площадь поверхности шара с радиусом =", a, "равна 4πR² =", fig4(a))
        print("Объём шара с радиусом =", a, "равна ⁴/₃πR³ =", ob4(a))
        
if __name__ == '__main__':
    main()
