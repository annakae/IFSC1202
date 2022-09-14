x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))

if x < y and x < z :
    smallest = x
elif y < x and y < z :
    smallest = y
elif z < x and z < y :
    smallest = z

if x < y and x > z :
    middle = x
elif x > y and x < z :
    middle = x
elif y < x and y > z :
    middle = y
elif y > x and y < z :
    middle = y
elif z < x and z > y :
    middle = y
elif z > x and z < y :
    middle = y

if x > y and x > z :
    largest = x
elif y > x and y > z :
    largest = y
elif z > x and z > y :
    largest = z

print(smallest, middle, largest)