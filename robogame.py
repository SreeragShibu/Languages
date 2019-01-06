x=input()
xi=int(x)
final=[]
for k in range(xi):
    y=input()
    #print(xi)
    unsafe=0
    #print(type(xi))
    #print(y)
    ind=list()
    val=list()
    indcount={}
    #print(type(y))
    numcount=0
    count=-1
    dc=-1
    for i in y:
        count+=1
        #print(i)
        if(i!="."):
           dc+=1
           numcount+=1
           indcount[count]=int(i)
    #print(numcount)
    #print(indcount)
    ind=list(indcount.keys())
    val=list(indcount.values())
    #print(ind)
#    for i in ind:
        #print(i)

#   for i in indcount:
        #print(i);

    if(numcount<2):
        final.append("safe")
    else:
        f=0
        n=1
        c=0
        while(unsafe==0):
            c+=1
            if(c==numcount):
                break
            if(ind[n]-ind[f]>=val[n]+val[f]):
                if((ind[n]-ind[f]+1)%2==1):
                    unsafe=1
                    break
            f+=1
            n+=1

        if(unsafe==1):
            final.append("unsafe")
        else:
            final.append("safe")


for i in final:
    print(i)
