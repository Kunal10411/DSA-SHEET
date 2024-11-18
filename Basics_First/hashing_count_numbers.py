
n=int(input("enter the size of array:\n"))
arr=[]
for i in range(n):
    arr.append(int(input("enter the element:\n")))
    print(arr)

def hash(arr):
    count = [0] * 100  # Initialize a list of size 12 with all elements set to 0
    for num in arr:   # Iterate through each number in the input array
        if num < len(count):  # Check if the number is less than 12
            count[num] += 1  # Increment the count at the index corresponding to the number
    return count

q=int(input("enter the number of queries:\n"))
for i in range(q):
    x=int(input("enter the number to be checked:\n"))
    print(hash(arr)[x])
