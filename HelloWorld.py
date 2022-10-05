fileToRead="06.04 EmptyLinesInput.txt"
fileToWrite="06.04 EmptyLinesOutput.txt"
fout=open(fileToWrite,"w")
readCount=0
writeCount=0
with open(fileToRead,"r") as f:
    for line in f:
        readCount+=1
        if line.strip():
            writeCount+=1
            fout.write(line)
fout.close()
print(readCount,'records read')
print(writeCount,'records written')

for i in range(len(lsta)):
    if(lsta[i] != lstb[i]):
        print(f"Line: {i+1} - {lsta[i]}")
        print(f"Line: {i+1} - {lstb[i]}")
        count += 1