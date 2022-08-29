from math import ceil
a = int(input("Enter Classroom A: "))
b = int(input("Enter Classroom B: "))
c = int(input("Enter Classroom C: "))

d = ceil(a/2) + ceil(b/2) + ceil(c/2)
print(d)

