
#Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N.
#  Find the number(between 1 to N), that is not present in the given array.

def find_missing_number(arr, n):
    # XOR of all elements in the array
    array_xor = 0
    for num in arr:
        array_xor ^= num

    # XOR of all numbers from 1 to n
    total_xor = 0
    for i in range(1, n + 1):
        total_xor ^= i

    # XOR of the above two results gives the missing number
    return total_xor ^ array_xor

# Example usage
arr = [1, 2,3, 4, 5,7]
n = 7
print("The missing number is:", find_missing_number(arr, n))
