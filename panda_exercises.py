import pandas as pd

a = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

fruits = pd.Series(a)

#1.Determine the number of elements in fruits.

len(a)

#2 Output only the index from fruits.

list(fruits.index)

#3. Output only the values from fruits.
fruits.values

#4. Confirm the data type of the values in fruits.
fruits.dtype

import random
#5. Output only the first five values from fruits. 
#Output the last three values. Output two random values from fruits.
fruits.head(5), fruits.tail(3), fruits.sample(2)

#6. Run the .describe() on fruits to see what 
#information it returns when called on a Series with string values.

fruits.describe()

#7 Run the code necessary to produce only the unique string values from fruits.
fruits.unique()

#set(fruits.values) -another way to solve 

#8 Determine how many times each unique string value occurs in fruits.

fruits.nunique() 

#len(fruits.unique())

#9 Determine the string value that occurs most frequently in fruits.
###max(fruits)

fruits.value_counts().head(1)

#10 Determine the string value that occurs least frequently in fruits.

fruits.value_counts().nsmallest(n=1, keep='all')

#1. Capitalize all the string values in fruits.

fruits.str.capitalize()

#2 Count the letter "a" in all the string values (use string vectorization).

fruits.str.count('a')

#LAMBDA WAY OF SOLVING # 2
fruits.apply(lambda x: x + 'count of a: ' + str(x.count('a')))

vowels =['a', 'e','i','o','u']
vowel_count = 0
for let in fruit:
    if let in vowels:
        vowel_count += 1

len([let for let in fruit.lower() if let in ['a','e','i','o','u']])

#3 Output the number of vowels in each and every string value.
def count_vowels(some_word):

    return len([let for let in some_word.lower() if let in ['a','e','i','o','u']])

fruits.apply(count_vowels)

#4 Write the code to get the longest string value from fruits.

# fruits.str.len().max()
#fruits.str.len() == fruits.str.len().max()
bool_mask = fruits.str.len() == fruits.str.len().max()
fruits[bool_mask]

#5 Write the code to get the string values with 5 or more letters in the name.

fruits[fruits.str.len() >= 5]

#6 Find the fruit(s) containing the letter "o" two or more times.


fruits[fruits.str.lower().str.count('o') >= 2]
#case sensitive 
#fruits[frutis.str.lower().str.count('o') >= 2]

#7 Write the code to get only the string values containing the substring "berry".

fruits.apply(lambda x:'berry' in x)
fruits[fruits.apply(lambda x:'berry' in x)]

#8 Write the code to get only the string values containing the substring "apple".
apple_mask = fruits.str.contains('apple')
fruits[apple_mask]

#9 Which string value contains the most vowels?
fruits[fruits.apply(count_vowels)]

most_vowels = fruits.applyfruits.apply(count_vowels)== fruits.apply(count_vowels).max()

#1
letters = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'

letters = pd.Series(list(letters))

letters.value_counts().head(1)

# idxmax will give us the index associated with 
letters.value_counts().idxmax()
#2. Which letter occurs the Least frequently?
letters.value_counts().nsmallest(n=1,keep='all')

#3. How many vowels are in the Series?
def is_vowel(some_word):
    return some_word in ['a', 'e', 'i', 'o', 'u']

letters.str.lower().apply(is_vowel).sum()

#4. How many consonants are in the Series?

# apply the idea of 'not' to every instance in the Series output by my vowel check
(~letters.str.lower().apply(is_vowel)).sum()

#5. Create a Series that has all of the same letters but uppercased.
# use a differenter string method on it
letters.str.upper()

#6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.
import matplotlib.pyplot as plt
letters.value_counts().head(6).plot(kind='barh')
plt.title('top six all time letters objective best, do not dispute please and thank you')
plt.show()

#1. What is the data type of the numbers Series?
numbers = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
type(numbers)
numbers = pd.Series(numbers)
#2. How many elements are in the number Series?
numbers.nunique()
#3. Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
numbers = numbers.str.replace('$', '').str.replace(',','').astype(float)

#4. Run the code to discover the maximum value from the Series.
numbers.max()
#5. Run the code to discover the minimum value from the Series.
numbers.min()
#6. What is the range of the values in the Series?
numbers.max() - numbers.min()
#7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
pd.cut(numbers, 4).value_counts().sort_index()
#8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
pd.cut(numbers, 4).value_counts().sort_index().plot(kind='barh')
plt.title('4 bins')
plt.xlabel('count')
plt.ylabel('$ bins')
plt.show()

#1. How many elements are in the exam_scores Series?
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
type(exam_scores)

#2. Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
exam_scores.max(), exam_scores.min(), exam_scores.mean(), exam_scores.median()

#3. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
exam_scores.plot.hist()
plt.title('Distribution of Exam Scores')
plt.xlabel('Scores')
plt.show()
#4. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
100 - exam_scores.max()
# curved grades will be assigned the original scores
# plus the difference between the highest grade and a perfect score
curved_grades = exam_scores + (100 - exam_scores.max())
#5. Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
bin_edges = [0, 70, 75, 80, 90, 100]
bin_labels = ['F', 'D', 'C', 'B', 'A']
letter_grades = pd.cut(curved_grades, bins=bin_edges, labels=bin_labels)
#6. Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
letter_grades.value_counts().sort_index().plot.barh()
plt.title('Curved Letter Grade Distribution')
plt.show()