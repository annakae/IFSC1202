sum = 0

while True:
    n = int(input("Enter a Number (zero to quit): "))
    sum += n
    if n == 0: 
        break

print("Sum:", sum)