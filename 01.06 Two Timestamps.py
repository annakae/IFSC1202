print("First Timestamp")

a = int(input("Enter Hours: "))
b = int(input("Enter Minutes: "))
c = int(input("Enter Seconds: "))

print("Second Timestamp")

d = int(input("Enter Hours: "))
e = int(input("Enter Minutes: "))
f = int(input("Enter Seconds: "))

g = a*3600 + b*60 + c
h = d*3600 + e*60 + f

print(h-g)