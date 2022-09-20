n = 0

while True:
    x = int(input("Enter a Number (zero to quit): "))
    if x == 0: 
        break
    if x % 2 == 0:
        n += 1

print("Number of Even Values:", n)