x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))

if x == y and x == z :
    print("3")
elif x == y and x != z :
    print("2")
elif x != y and x == z :
    print("2")
elif y != x and y == z :
    print("2")
else:
    print("0")