


def largest(arr):
    n=len(arr)
    slarge=-1
    large=arr[0]
    for i in range(0,n):
        if arr[i]>large:
            slarge=large
            large=arr[i]
    
        elif arr[i]>slarge and arr[i]!=large:
            slarge=arr[i]
    return slarge        


n=int(input("enter the size of the array:\n"))
arr=[]
for _ in range(n):
    x=int(input("enter the elements:\n"))
    arr.append(x)
    print(arr)

print("secordlargest is:",largest(arr))
    
