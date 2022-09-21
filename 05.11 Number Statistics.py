count = 0
sum = 0
av = 0
min = 100
max = 0

while True:
    n = int(input("Enter a Value (zero to quit): "))
    if n == 0: 
        break

    count += 1
    sum += n
    av += 1
    
    if n < min:
        min = n
    if n > max:
        max = n
   
print("Count: {:>3}".format(count))
print("Sum: {:>8.1f}".format(sum))
print("Average: {}".format(sum / av))
print("Minimum: {:.1f}".format(min))
print("Maximum: {:.1f}".format(max))