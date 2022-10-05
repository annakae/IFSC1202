file = open("06.03 FTemps.txt", "r")
num = 0

for f in file:
    c = (float(f) - 32) * 5/9
    c = round(c,1)
    f = open("06.03 CTemps.txt", "a")

    f.write(str(c))
    f.write('\n')
    f.close()

    num = num + 1

print(str(num)+" records written")