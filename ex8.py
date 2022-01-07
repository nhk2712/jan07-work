s = input("Type something: ")
sl = s.split()
res=""

for i in range(len(sl)-1):
    res+=sl[i]+" "
res+=sl[len(sl)-1]

print(res)