x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))

if x == y and x != z :
    print("3")
elif x == z and x != y :
    print("2")
else:
    print("1")