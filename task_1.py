def comparison(a: int, b: int):
    if a > b:
        print(">")
    elif a == b:
        print("=")
    else:
        print("<")

number_one = input("Введите число a\n")
number_two = input("Введите число b\n")
comparison(int(number_one), int(number_two))