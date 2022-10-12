s = str(input("Enter a string: "))

a = s.find('h')
a += 1
b = s.rfind('h')
if(a==b):
    print(a)
else:
    print(s[:a])

t = s[a:b]
print(t[::-1])
print(s[b:])