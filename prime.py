
def primeano(n):
    sq=int(n**0.5)+1
    print(sq)
    for i in range(2,sq):
        if(n%i==0):
            return 0
    return 1



n=int(input())
if(primeano(n)==1):
    print("Prime")
else:
    print("not prime")
