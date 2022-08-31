x = int(input("Enter First 2 Digit Number: "))
a = int(input("Enter Second 2 Digit Number: "))

y = (x % 100) // 10
b = (a % 100) // 10
z = x % 10
c = a % 10

print("Merged Number: {}{}{}{}" .format(y,b,z,c))