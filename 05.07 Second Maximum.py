first = int(input("Enter First Number: "))
second = int(input("Enter Second Number: "))

max = 0
x = 0
a = True

while True:
    n = int(input("Enter a Number (zero to quit): "))
    if n == 0:
        break
    if a or max < n:
        max = n
        x = 1
    elif max == n:
        x += 1
    a = False

print("First Maximum:", max)
print("Second Maximum:", x)