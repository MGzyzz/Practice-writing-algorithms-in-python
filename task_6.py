a = [10, 26, 7, 77, 20, 54, 40, 46, 54, 63]
b = [18, 55, 95, 94, 11, 33, 44, 79, 8, 55]
c = []

count_1 = 0
count_2 = 0

while True:
    c.append(a[count_1] + b[count_2])
    count_1 += 1
    count_2 += 1
    if len(c) == len(a):
        break

print(f"MAX = {max(c)}")
