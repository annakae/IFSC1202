max = -1
smax = -1
y = -1
x = 1
n = 1

while n != 0:
    n = int(input("Enter First Number: "))
    n = int(input("Enter Second Number: "))
    break

while True:
    n = int(input("Enter a Number (zero to quit): "))
    if n == 0:
        break
    y = max
    if n == max:
        x += 1
    elif n > max:
        max = n 
    elif smax <= n <= max:
        smax = n 
    if smax < y < max:
        smax = y

print("First Maximum:", max)

if smax != -1:
    print("Second Maximum:", smax)