def count(arr):
    frequency_map={}
    
    for element in arr:
        if element in frequency_map:
            frequency_map[element]+=1

        else:
            frequency_map[element]=1
    return frequency_map


n=int(input("enter the size of the array:\n"))
arr=[]
for _ in range(n):
    x=int(input("enter the elements:\n"))
    arr.append(x)
    print(arr)

frequency_map=count(arr)    
print(frequency_map)