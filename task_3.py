def discharges(a: int):
    return f"{(a // 1000) * 1000}\n{((a % 1000) // 100) * 100}\n{((a % 100) // 10) * 10}\n{(a % 10)}"

number = input("Введите четырехзначное число\n")
print(discharges(int(number)))

