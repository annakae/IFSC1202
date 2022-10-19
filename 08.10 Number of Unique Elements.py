inputlist = list()
input = input("Enter Values Seperated by Spaces: " ).split()
n = len(input)

for i in range(n):
    inputlist.append(int(input[i]))

for i in range(n):
    count = 1
    for j in range(n):
        if inputlist[i] == inputlist[j] and i != j:
            count += 1
    if count == 1:
        print("Unique Elements: " ,inputlist[i])