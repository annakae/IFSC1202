fileread="06.04 EmptyLinesInput.txt"
filewrite="06.04 EmptyLinesOutput.txt"
fout = open(filewrite,"w")

read = 0
write = 0

with open(fileread,"r") as f:
    for line in f:
        read += 1

        if line.strip():
            write += 1
            fout.write(line)

fout.close()

print(read,'records read')
print(write,'records written')