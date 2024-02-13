def triangle(a: int, b:int, c:int):
    if a + b > c:
        if a + c > b:
            if a + c > b:
                return "Yes"
            else:
                return "No"
        else:
            return "No"
    else:
        return "No"

number_one = input("Введите число a\n")
number_two = input("Введите число b\n")
number_three = input("Введите число c\n")

print(triangle(int(number_one), int(number_two), int(number_three)))