years = 365
month = 30
num = int(input("Пожалуйста введите свой возраст в днях\n"))

count_1 = 0
year = round(num/years)
num = num % years
days = num % month
months = num // month
if months < 1:
    months = 0
age = {'years': year, 'month': months, 'days': days}
print(age)