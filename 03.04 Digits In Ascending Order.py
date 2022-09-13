x = int (input("Enter a Number: "))

a = x // 100
b = (x % 100) // 10
c = x % 10

if a < b and a < c and b < c :
    print("YES")
else:
    print("NO")