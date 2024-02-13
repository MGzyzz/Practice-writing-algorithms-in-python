number_one = input("Введите первое число\n")
number_two = input("Введите второе число\n")

m = int(number_one)/int(number_two)
n = int(number_two)/int(number_one)
d = int(number_one) - int(number_two)

relationship = {'max_to_min': m, 'min_to_max': n, 'difference': d}
print(f"Max to Min = {m}\nMin to Max = {round(n, 2)}\nDifference = {d}")