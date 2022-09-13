x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))

smallest = 0

if x < y and x < z :
    smallest = x
elif y < z :
    smallest = y
else :
    smallest = z

print(smallest)