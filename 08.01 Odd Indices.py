x = input("Enter Values Seperated by Spaces: ")

def Split(mix):
    ev_li = []
    od_li = []
    for i in mix:
        if (i % 2 == 0):
            ev_li.append(i)
        else:
            od_li.append(i)
    print("Odd lists:", od_li)