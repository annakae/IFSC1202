values = input("Enter Values Seperated by Spaces: ")
lst = values.split(" ")
 
for i in range(0, len(lst)):
    if i % 2 != 0:
        print(i)