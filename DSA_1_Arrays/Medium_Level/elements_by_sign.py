#There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. 
# Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

#Note: Start the array with positive elements.

def rearrange(arr):
    n=len(arr)
    #separating +ve and -ve
    posi=[x for x in arr if  x>0]
    nega=[x for x in arr if  x<0]

    result=[]
    posi_index=0
    nega_index=0

    while posi_index < len(posi) and nega_index < len(nega):
        result.append(posi[posi_index])
        result.append(nega[nega_index])
        posi_index+=1
        nega_index+=1
    return result    





n= int(input("Enter the size of array:"))
arr=[]
for i in range(n):
    ele=int(input("Enter the elements:"))
    arr.append(ele)
    print(arr)

print(rearrange(arr))    