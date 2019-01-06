
def num_operations(arr,k):
    sum=0
    
    arr.sort()
    if(len(arr)>1):
        for i in range(len(arr)-1):
            if(arr[i]<=k):
                sum+=arr[i]
                
            else:
            
                diff=arr[i]-k
                arr[i+1]-=diff
                sum+=k
                
        sum+=arr[len(arr)-1]
    else:
        return arr[0]

    return sum






n=int(input())
ans=[]
for i in range(n):
    k=int(input().split()[1])
    l=input()
    arr=[ int(i) for i in l.split()]
    ans.append(num_operations(arr,k))

for i in ans:
    print(i) 