import re
fname=open("actual.txt")
sum=0.0

for line in fname:
    y=re.findall('[0-9]+',line);
    for inside in y:
        try:
            z=float(inside)
            sum+=z
        except:
            continue
print("the sum of numbers are:")
print(sum)
