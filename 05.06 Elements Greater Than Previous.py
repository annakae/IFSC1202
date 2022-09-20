n = 1
x = 0
y = 0
z = 0

while n != 0:
    n = int(input("Enter a Number (zero to quit): "))
    if n != 0: 
        if y == 0:
            x = n
        if n > x:
            z += 1
        y += 1
        x = n

print("Number of Values Greater Than the Previous:", z)