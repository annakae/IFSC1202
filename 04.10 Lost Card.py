n = int(input("Enter Number of Cards: "))
c = 0

for i in range(n-1):
    c -= int(input("Enter Card: "))

for i in range(1, n+1):
    c += i

print(c)