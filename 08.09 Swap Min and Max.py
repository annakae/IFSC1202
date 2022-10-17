s = input("Enter Values Seperated by Spaces: ") 
a = []
b = s.split(" ")
n = len(b)

for i in range(n):
    bb = (int)(b[i])
    a = a + [bb]

max = -9999
min = 9999
for i in range(n):
    if(a[i]>max):
        max = a[i]
        pos1 = i
    if(a[i] < min):
        min = a[i]
        pos2 = i

temp = a[pos1]
a[pos1] = a[pos2]
a[pos2] = temp

for i in a:
    print("Swapped Minimum and Maximum: ",i)