def linear(arr):
    n=len(arr)

    for i in range(n):
        if arr[i]==num:
            return i
        
    return -1

n = int(input("Enter the size of the array: "))
arr = []

for i in range(n):
    ele = int(input(f"Enter element {i + 1}: "))
    arr.append(ele)
    print(arr)
num=int(input("enter the number to be checked:"))    
    
print(linear(arr))    


