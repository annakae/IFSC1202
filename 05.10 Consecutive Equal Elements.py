n = 1
x = 0
y = 0

a = 0
b = None
c = 0

while n != 0:
    n = int(input("Enter a Number (zero to quit): "))
    if n != 0:
        if y == 0:
            x = n
            a = 1
        else: 
            if n == x:
                a += 1
            else:
                if a > c:
                    c = a
                    b = x
        y += 1
        x = n
print(b, "repeated", c, "times")