s = input("Enter Values Seperated by Spaces: ")
my_list_str = s.split()
my_list = []


for beta in my_list_str:
    my_list.append(int(beta))


found = False
for i in range(len(my_list) - 1):
  if my_list[i] > 0 and my_list[i + 1] > 0:
     print (my_list[i], end =' ')
     print (my_list[i + 1])
     found = True
     break
  elif my_list[i] < 0 and my_list[i + 1] < 0:     
      print (my_list[i], end =' ')
      print (my_list[i + 1])
      found = True
      break
    
if not found:
    print ('NONE')