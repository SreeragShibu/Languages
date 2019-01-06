
def num_operations(arr,k):
    sum=0
    #print(k)
    arr.sort()
    for i in range(len(arr)-1):
        if(arr[i]<=k):
            sum+=arr[i]
            #print("In 1")
        else:
            #print("In 2")
            diff=arr[i]-k
            arr[i+1]-=diff
            sum+=k
            #print(diff)
        #print(sum)
    sum+=arr[len(arr)-1]

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
