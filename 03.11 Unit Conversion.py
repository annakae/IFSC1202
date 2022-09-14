a = float(input("Enter From Value: "))

b = input("Enter From Unit (in, ft, yd, mi): ")
if b == "in, ft, yd, mi" :
    
else:
    print("From Unit is invalid")
    exit(0)

c = input("Enter To Unit (in, ft, yd, mi): ")
if c == "in, ft, yd, mi" :
    c == c
else:
    print("To Unit is invalid")
    exit(0)

if b == "in" and c == "ft" :
    x = a * round(0.08333333333, 7)
elif b == "in" and c == "yd" :
    x = a * round(0.027777777, 7)
elif b == "in" and c == "mi" :
    x = a * round(0.0000157, 7)
elif b == "in" and c == "in" :
    x = a * 1

if b == "ft" and c == "in" :
    x = a * 12
elif b == "ft" and c == "yd" :
    x = a * round(0.33333333,7)
elif b == "ft" and c == "mi" :
    x = a * round(0.0001893939393, 7)
elif b == "ft" and c == "ft" :
    x = a * 1

if b == "yd" and c == "in" :
    x = a * 36
elif b == "yd" and c == "ft" :
    x = a * 3
elif b == "yd" and c == "mi" :
    x = a * round(0.0005681818, 7)
elif b == "yd" and c == "yd" :
    x = a * 1

if b == "mi" and c == "in" :
    x = a * 63360
elif b == "mi" and c == "ft" :
    x = a * 5280
elif b == "mi" and c == "yd" :
    x = a * 1760
elif b == "mi" and c == "mi" :
    x = a * 1

print("{} {} => {:<.6} {}".format(a,b,x,c))