x = input("Enter Values Seperated by Spaces: ")
x_list = x.split()

x_distinct = len(set(x_list))

print("Number of Distinct Elements: ", x_distinct)