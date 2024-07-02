n = int(input("Enter the number:"))
dt = {
    1:3,
    2:3,
    3:5,
    4:4,
    5:4,
    6:3,
    7:5,
    8:5,
    9:4,
}

temp = n
sum = 0
while temp > 0:
    rem = temp % 10
    sum += dt[rem]
    temp = temp // 10
if n > 100:
    sum += 10
print(sum)
    