string = set(input("enter a string"))

s = set()
a = 97
for i in range(26):
    s.add(chr(a+i))
    print(chr(i+a))

if (string & s) == s: print("its a panagram")