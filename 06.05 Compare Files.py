fa = open("06.05 CompareFileA.txt")
fb = open("06.05 CompareFileB.txt")

lsta = []
lstb = []

for l in fa:
    lsta.append(l)

for l in fb:
    lstb.append(l)

count = 0

for i in range(len(lsta)):
    if(lsta[i] != lstb[i]):
        print(f"Line: {i+1} - File A: {lsta[i]}")
        print(f"Line: {i+1} - File B: {lstb[i]}")
        count += 1

print(count, "differences")

fa.close()
fb.close()