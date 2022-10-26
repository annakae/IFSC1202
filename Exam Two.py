file_read = open("Exam Two Names.txt", 'r')

boy_names = []
girl_names = []

for line in file_read.readlines():
    data = line.strip().split(',')
    boy_names.append(data[0].strip())
    girl_names.append(data[1].strip())

file_read.close()

name = input('Enter a Name: ').strip()
while name.lower() != 'q':
    name = name[0].upper() + name[1:].lower()
    
    if name in boy_names:
        print('Boy\'s Name - Rank', boy_names.index(name) + 1)
    elif name in girl_names:
        print('Girl\'s Name - Rank', girl_names.index(name) + 1)
    else:
        print('Name Not Found')

    name = input('Enter a Name: ').strip()