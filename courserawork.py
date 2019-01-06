name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
ls=list()
for line in handle:
    if line.startswith("From"):
        str=line.split()
        if len(str)<3: continue
        ls.append(str[5].split(":")[0])
counts=dict()
for ch in ls:
    counts[ch]=counts.get(ch,0)+1
print(ls)
lis=list()
for k,v in counts.items():
    tup=(k,v)
    lis.append(tup)
lis=sorted(lis)
for i in lis:
    print(i[0],counts[i[0]])
