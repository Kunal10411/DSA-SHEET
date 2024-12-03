#This problem has 3 variations. They are stated below:
#Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.
#Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.
#Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.

#Example 1:
# Input Format:
 # N = 5, r = 5, c = 3
#Result: 6 (for variation 1)
# 1 4 6 4 1 (for variation 2)

# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1    (for variation 3)

# Explanation:
 # There are 5 rows in the output matrix. Each row is formed using the logic of Pascal’s triangle.

def pascal(N,R,C):    # 1st answer function
    res=1
    for i in range(R):
        res=res* (N-i)
        res=res // (i+1)
    return res    

def pascal2(N,R):    #2nd answer variation
    for i in range(R + 1):  # Loop through rows
        ans = 1  # Reset ans for each row
        for j in range(1, i + 1):  # Calculate each value in the row
            ans = ans * (N - j) // j
            print(ans)    

def generate_pascals_triangle(N): # 3rd answwer Variation
    # Generate Pascal's Triangle up to N rows
    triangle = []
    for i in range(N):
        row = [1]  # First element is always 1
        for j in range(1, i):
            # Each element is the sum of two elements above
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        if i > 0:  # Add the last 1 if i > 0
            row.append(1)
        triangle.append(row)
    return triangle


N=int(input("Enter the rows for pascal traingle:"))
C=int(input("Enter the Column for answer:"))
R=int(input("Enter the rows for answer:"))

print(generate_pascals_triangle(N))