n=int(input("enter the size of the array:\n"))
arr=[]
for _ in range(n):
    x=int(input("enter the elements:\n"))
    arr.append(x)
    print(arr)

print(sorted(arr))    


def sort(arr):
    n=len(arr)
    
   
    for i in range(n):
        min_index=i

        for j in range(i+1,n):
            if arr[j]< arr[min_index]:
                min_index=j

        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr    
