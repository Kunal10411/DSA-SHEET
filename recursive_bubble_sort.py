def recursive_bubbble(arr,n=None):
    if n is None:
        n=len(arr)
    if n==1:
        return
    
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]

    recursive_bubbble(arr,n-1)

n=int(input("enter the size of the array:"))
arr=[]
for _ in range(n):
    ele=int(input("enter the elements:"))
    arr.append(ele)
    print(arr)

recursive_bubbble(arr)
print(arr)










