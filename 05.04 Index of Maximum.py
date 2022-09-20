highest = 0
x = 0
y = 0

while True:
    n = int(input("Enter a Number (zero to quit): "))
    if n == 0:
        break
    x += 1
    if n > highest:
        highest, y = n, x

print ("Maximum:", highest)
print("Index of Maximum:", y)