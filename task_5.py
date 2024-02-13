border = ''
house = ''
print("Введите координаты точки Раздела")
border_x = input("Первая координата:\n")
border_y = input("Вторая координата:\n")

print("Введите координаты вашего дома")
house_x = input("Первая координата:\n")
house_y = input("Вторая координата:\n")

coordinates = {'border_x': border_x, 'border_y': border_y, 'house_x': house_x, 'house_y': house_y}
if int(border_x) >= 0 and int(border_y) <= 0:
    border = border + 'SE'
elif int(border_x) >= 0 and int(border_y) >= 0:
    border = border + "NE"
elif int(border_x) <= 0 and int(border_y) >= 0:
    border = border + "NW"
else:
    border = border + "SW"

if int(house_x) >= 0 and int(house_y) <= 0:
    house = house + 'SE'
elif int(house_x) >= 0 and int(house_y) >= 0:
    house = house + "NE"
elif int(house_x) <= 0 and int(house_y) >= 0:
    house = house + "NW"
else:
    house = house + "SW"

if border == house:
    print("border")
elif house == "NW":
    print("NW")
elif house == "NE":
    print("NE")
elif house == "SW":
    print("SW")
else:
    print("SE")


