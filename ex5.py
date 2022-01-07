s = input("Type something: ")

res = []

for i in range(len(s)):
    if s[i] == "a":
        res.append(i)

for i in range(len(res)):
    print(" ",res[i],end="")

print("\n ",len(res))