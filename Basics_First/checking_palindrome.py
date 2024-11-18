def palin(i):
    if i >= n // 2:
        return True
    else:
        # Check if characters are not equal
        if s[i] != s[n - i - 1]:
            return False  # Return False if not a palindrome
        return palin(i + 1)  # Recursive call to check the next characters

n = int(input("enter the size of String \n"))
s = []
for i in range(n):
    s.append(input("enter the element \n"))
    print(s)

# Print whether the string is a palindrome or not
if palin(0):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")