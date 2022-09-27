import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#1/2. How many negative and positive numbers are there?

negative_numbers = a < 0
total_neg_num = np.count_nonzero(negative_numbers == True)
total_pos_num = np.count_nonzero(negative_numbers == False)


print('Negative numbers:', total_neg_num)
print('Positive numbers:', total_pos_num)

#3. How many even numbers are there?

even_numbers = a % 2 == 0
total_even_num = np.count_nonzero(even_numbers == True)
print(total_even_num)

#4. If you were to add 3 to each data point, how many positive numbers would there be?

new_a = np.array([n + 3 for n in a])

new_a_greater = new_a > 0

greater_count = np.count_nonzero(new_a_greater == True)


print(greater_count)

#5. If you squared each number, what would the new mean and standard deviation be?

squares = a ** 2
squaresdev = np.std(squares)
squaresmean = np.mean(squares)

print('Std Dev:',squaresdev)
print('Mean:',squaresmean)

#6. A common statistical operation on a dataset is centering. 
#This means to adjust the data such that the mean of the data is 0. 
#This is done by subtracting the mean from each data point. Center the data set. 

mean_a = np.mean(a)

center_data = mean_a - a

print(center_data)

#7. Calculate the z-score for each data point. 

z_score = (a-mean_a)//(np.std(a))

print(z_score)

# extra Exercises 

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum(a)



# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min(a)
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max(a)
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

sum(a) / len(a)
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
prod_a

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

[n ** 2 for n in a]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
[n for n in a if n % 2 != 0]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
[n for n in a if n % 2 == 0]

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]


b2 = np.array(b)


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

b2.sum()
# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

b2.max()

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

b2.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

np.square(b2)

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

b2[b2 % 2 != 0]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
b2[b2 % 2 == 0]
# Exercise 9 - print out the shape of the array b.
b2.shape
# Exercise 10 - transpose the array b.
b2.transpose()
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b2.reshape(1,6)
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b2.reshape(6,1)
## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array(c)

c.min(), c.max(), c.sum(), c.prod()
# Exercise 2 - Determine the standard deviation of c.
c.std()
# Exercise 3 - Determine the variance of c.
c.var()
# Exercise 4 - Print out the shape of the array c
c.shape
# Exercise 5 - Transpose c and print out transposed result.
c.transpose()
# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c, c)
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
np.sum(c * c.transpose())
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
np.prod(c * c.transpose())

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)
# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)
# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)
# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)
# Exercise 4 - Find all the negative numbers in d
d[d < 0]
# Exercise 5 - Find all the positive numbers in d
d[d>0]
# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)
# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))
# Exercise 8 - Print out the shape of d.
d.shape
# Exercise 9 - Transpose and then print out the shape of d.
d.transpose().shape
# Exercise 10 - Reshape d into an array of 9 x 2
np.reshape(d, (9,2))