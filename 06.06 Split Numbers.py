def isEven(num):
    return num % 2 == 0
  
def isOdd(num):
    return num % 2 != 0
 
def isPrime(num):
    flag = False
    if(num == 1):
        return False
        
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    return (not flag)

inputFile = open("06.06 Numbers.txt","r")

evenNumbers = open("06.06 Evennumbers.txt","w+")
oddNumbers = open("06.06 Oddnumbers.txt","w+")
primeNumbers = open("06.06 Primenumbers.txt","w+")

countnum = 0
countOdd = 0
countEven = 0
countPrime = 0

for line in inputFile:
    line = int(line.strip())
    countnum += 1

    if isEven(line):
        evenNumbers.write(str(line) + "\n")
        countEven += 1
 
    elif isOdd(line):
        oddNumbers.write(str(line) + "\n")
        countOdd += 1
      
    if isPrime(line):
        primeNumbers.write(str(line) + "\n")
        countPrime += 1

inputFile.close()        
evenNumbers.close()
oddNumbers.close()
primeNumbers.close()

print(countEven,"even numbers")
print(countOdd,"odd numbers")
print(countPrime,"prime numbers")
print(countnum,"number read")