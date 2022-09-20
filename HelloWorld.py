highest = 0
index = 0

while True:
    num = int(input("Enter a Number (zero to quit): "))
    if (num==0):
        break
    if num > highest:
        highest = num

print ("Maximum:", highest)
