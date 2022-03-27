#1. Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся
# пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы
# должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль,
# если он ввел его в качестве делителя.


print("Выберите математическое действие")
while True:
  s = input("Сложение +, Вычитание -, Умножение *, Деление /+): ")
  if s == '0': break
  if s in ('+','-','*','/'):
    x = float(input("Введите х ="))
    y = float(input("Введите y="))
    if s == '+':
      print("Результат сложения = %.2f" % (x+y))
    elif s == '-':
      print("Результат вычитания = %.2f" % (x-y))
    elif s == '*':
      print("Результат умножения = %.2f" % (x*y))
    elif s == '/':
      if y != 0:
        print("Результат деления = %.2f" % (x/y))
      else:
        print("Делить на ноль нельзя!")
  else:
    print("Неверный знак операции!")

