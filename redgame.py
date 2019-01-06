def num_operation(arr,k):
    arr.sort()
    sum=0
    if(len(arr)>2):
        for i in range(len(arr)-1):
            if(arr[i]>k):
                val=k
            else:
                val=arr[i]
            sum+=val
        sum+=arr[len(arr)-1]
    else:
        max_val=max(arr)
        min_val=min(arr)
        val=0
        if(min_val>k):
            sum+=k
            val=k
        else:
            sum+=min_val

        sum+=max_val-val



    return sum






n=int(input())
ans=[]
for i in range(n):
    k=int(input().split()[1])
    l=input()
    arr=[ int(i) for i in l.split()]
    ans.append(num_operation(arr,k))

for i in ans:
    print(i)
