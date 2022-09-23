#1.Determine the number of elements in fruits.

len(a)

#2 Output only the index from fruits.

list(fruits.index)

#3. Output only the values from fruits.
list(fruits)

#4. Confirm the data type of the values in fruits.
type(fruits)

import random
#5. Output only the first five values from fruits. 
#Output the last three values. Output two random values from fruits.
list(fruits[0:5]), list(fruits[14:17]), random.sample(a, 2)

#6. Run the .describe() on fruits to see what 
#information it returns when called on a Series with string values.

fruits.describe()

#7 Run the code necessary to produce only the unique string values from fruits.
fruits.unique()

#8 Determine how many times each unique string value occurs in fruits.

fruits.nunique() 

#len(fruits.unique())

#9 Determine the string value that occurs most frequently in fruits.
max(fruits)

#10 Determine the string value that occurs least frequently in fruits.
fruits.min()

#1. Capitalize all the string values in fruits.

fruits.str.capitalize()

#2 Count the letter "a" in all the string values (use string vectorization).

#Series.str.count(pat, flags=0)[source]

a_in_each_word = fruits.str.count('a')

total_number = sum(fruits.str.count('a'))

#3 Output the number of vowels in each and every string value.

#Series.str.count(pat, flags=0)[source]
vowels =list('aeiou')

fruits.str.count('vowels')

WRONG FIX 

#4 Write the code to get the longest string value from fruits.

fruits.str.len().max()

NEED TO GET NAME OF STRING 

#5 Write the code to get the string values with 5 or more letters in the name.


#6 Find the fruit(s) containing the letter "o" two or more times.

#7 Write the code to get only the string values containing the substring "berry".

#8 Write the code to get only the string values containing the substring "apple".

#9 Which string value contains the most vowels?