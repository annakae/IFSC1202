str = input ("Enter a string : ")

strr = str[::-1]
index1 = str.find('f')

if index1 == -1:
  print(0)
else:
  index = strr.find('f')
  n = len(str)
  index2 = n - index

  if index1 == index2:
    print (index1)
  else:
    print (index1, index2)