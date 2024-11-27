


def largest(arr):
    slarge=-1
    large=arr[0]
    for i in range(1,n):
        if arr[i]>large:
            large=arr[i]
    return large

    for j in range(0,n):
        if arr[j]>slarge and arr[j]!=large:
            arr[j]=slarge
    return slarge        


n=int(input("enter the size of the array:\n"))
arr=[]
for _ in range(n):
    x=int(input("enter the elements:\n"))
    arr.append(x)
    print(arr)
print("largest is:",largest(arr))
print("secordlargest is:",largest(arr))
    
