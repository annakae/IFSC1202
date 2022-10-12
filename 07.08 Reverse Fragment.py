s = str(input("Enter a string: "))

a = s.find('h')
a += 1
b = s.rfind('h')
if(a==b):
    print(a)
else:
    t = s[a:b]
print(s[:a] + t[::-1] + s[b:])