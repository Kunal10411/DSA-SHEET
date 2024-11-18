def rotateleft(arr):
    temp=arr[0]
    n=len(arr)

    for i in range(1,n):
        arr[i-1]=arr[i]

    arr[i-1]=temp
    return arr    


n=int(input("enter the size of the array:"))
arr=[]
for i in range(n):
    ele=int(input("enter the element:"))
    arr.append(ele)
    print(arr)

print(rotateleft(arr))    