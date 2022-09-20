a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = 1

for i in range(a, b+1):
    c = i * i
    print("{}*{}={}".format(i,i,c))