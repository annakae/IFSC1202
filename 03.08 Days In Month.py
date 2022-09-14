x = int(input("Enter Month: "))

if x in {1, 3, 5, 7, 8, 10, 12} :
    print("31")
elif x in {4, 6, 9, 11} :
    print("30")
elif x in {2} :
    print("28")
else:
    print("Please enter an integer between 1-12")