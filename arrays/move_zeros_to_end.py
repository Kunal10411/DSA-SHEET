def move_zeros_to_end(arr):
    n = len(arr)
    j = 0  # Pointer to track the position to swap non-zero elements

    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr

# Input from the user
n = int(input("Enter the size of the array: "))
arr = []

for i in range(n):
    ele = int(input(f"Enter element {i + 1}: "))
    arr.append(ele)

print("Original array:", arr)
print("Array after moving zeros to the end:", move_zeros_to_end(arr))
