x = int(input("Enter Month: "))

if x in {1, 3, 5, 7, 8, 10, 12} :
    month = 31
elif x in {4, 6, 9, 11} :
    month = 30
elif x in {2} :
    month = 28

y = int(input("Enter Day: "))

if y < month :
    y = y + 1
else:
    y = 1
    if x == 12 :
        x = 1
    else:
        x = x + 1

print("Next Day: {}/{}" .format(x, y))