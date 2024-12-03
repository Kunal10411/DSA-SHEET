#The union of two arrays can be defined as the common and distinct elements in the two arrays.
# NOTE: Elements in the union should be in ascending order.

#Example 1:

# Input:

# n = 5,m = 5.
# arr1[] = {1,2,3,4,5}  
# arr2[] = {2,3,4,4,5}
# Output: {1,2,3,4,5}

#Explanation: 

#Common Elements in arr1 and arr2  are:  2,3,4,5
#Distnict Elements in arr1 are : 1
#Distnict Elemennts in arr2 are : No distinct elements.
#Union of arr1 and arr2 is {1,2,3,4,5} 

def union(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    arr3=set()
    
    
    for i in list(arr1):
        if i not in arr3:
            arr3.add(i)
    for j in list(arr2):
        if j not in arr3:
            arr3.add(j)    
    
    return arr3            

def common(arr1,arr2):
    arr4=set()
    for i in arr1:
        if i in arr2:
            arr4.add(i)
            
        
    return arr4





arr3=set()
n=int(input("enter the size of the array1:"))
arr1=set()

for i in range(n):
    ele1=int(input("enter the element:"))
    arr1.add(ele1)
    print(arr1)

m=int(input("enter the size of the array2:"))
arr2=set()
for i in range(m):
    ele2=int(input("enter the element:"))
    arr2.add(ele2)
        
print("First array",arr1)
print("second array",arr2)
print(union(arr1,arr2))
print("common:",common(arr1,arr2))