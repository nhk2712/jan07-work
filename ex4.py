s = input("Type something: ")

for i in range(len(s)):
    if s[i] == " ":
        print(i)
        break