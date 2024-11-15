def rotate_by_D(arr,d):
    n = len(arr)  # Calculate the length of the array
    temp = arr[:d]  # Store the first d elements in temp
    for i in range(d, n):
        arr[i - d] = arr[i]

    for i in range(n - d, n):
        arr[i] = temp[i - (n - d)]

    return arr

# Change 'n' to 'arr' in the function call
arr = [1, 4, 5, 3, 2]  # Define arr
print(rotate_by_D(arr, 3))