x = int(input("Enter a Number: "))

a = x // 1000
b = (x % 1000) // 100
c = (x % 100) // 10
d = x % 10

if a == d and b == c :
    print("YES")
else:
    print("NO")