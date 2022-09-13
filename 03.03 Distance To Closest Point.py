a = int(input("Enter Point A: "))
b = int(input("Enter Point B: "))
c = int(input("Enter Point C: "))

closest = 0

if a > b :
    x = a - b
else:
    x = b - a

if a > c :
    y = a - c
else:
    y = c - a

if x < y :
    closest = x
elif x > y :
    closest = y

print(closest)