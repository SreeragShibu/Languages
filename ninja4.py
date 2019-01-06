def primeano(n):
    sq=int(n**0.5)+1
#    print(sq)
    for i in range(2,sq):
        if(n%i==0):
            return 0
    return 1

n=int(input())
s=list()
for i in range(n):
    k=int(input())
    s.append(k)
#print(s)
for i in s:
#    print("for ",i,"\n")
    p=list()
    c=0
    for k in range(2,i+1):
        if(primeano(k)==1):
#           print(k)
           c+=1
    if(c%2==0):
        print("Harshit")
    else:
        print("Aahad")
