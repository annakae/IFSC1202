x = int(input("Enter a 3 Digit Number: "))
y = 0

while (x > 0):
    z = x % 10
    y = y * 10 + z
    x = x // 10

print("Reverse of Digits: {}" .format(y))