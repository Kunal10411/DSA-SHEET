def bubble(arr):

    n=len(arr)
    

    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True

        if not swapped:
            break
    return arr    


n=int(input("enter the size of the array:\n"))
arr=[]
for _ in range(n):
    ele=int(input("enter the elements: "))
    arr.append(ele)
    print(arr)

print("sorted array:",bubble(arr))





