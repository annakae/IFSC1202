highest = 0

while True:
    n = int(input("Enter a Number (zero to quit): "))
    if n == 0:
        break
    if n > highest:
        highest = n

print ("Maximum:", highest)