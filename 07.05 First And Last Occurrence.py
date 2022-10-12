str = input ("Enter a string: ")
index1 = str.find('f')

if index1 == -1:
  print(0)
else:
  index = str.find('f')
  n = len(str)
  index2 = n - index - 1

  if index1 == index2:
    print (index1)
  else:
    print (index1, index2 - 2)