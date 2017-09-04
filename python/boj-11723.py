from sys import stdin

t = int(stdin.readline())
s = set()
for i in range(t):
    line = stdin.readline()
    if line[:2] == "ad":
        s.add(int(line.split()[1]))
    elif line[:2] == "ch":
        if int(line.split()[1]) in s:
            print(1) 
        else:
            print(0)
    elif line[:2] == "re":
        a = int(line.split()[1])
        if a in s:
            s.remove(a)
    elif line[:2] == "al":
        s = set(range(1, 21))
    elif line[:2] == "em":
        s = set()
    else:
        a = int(line.split()[1])
        if a in s:
            s.remove(a)
        else:
            s.add(a)
