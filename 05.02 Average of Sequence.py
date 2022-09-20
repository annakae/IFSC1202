sum = 0
x = 0

while True:
    n = int(input("Enter a Number (zero to quit): "))
    if n == 0:
        break
    sum += n
    x += 1
if x == 0:
    print("Sequence Length is 0")
else:
    print("Average:", sum / x)