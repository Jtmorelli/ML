""" 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
"""

from itertools import count
import string
from typing import Counter


int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter all even elements
even = list(filter(lambda x: x % 2 == 0, int_list))
print(even)

# Filter all odd elements
odd = list(filter(lambda x: x % 2, int_list))
print(odd)


""" 2)
find which days of the week have exactly 6 characters.
"""

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

six_letter_list = list(filter(lambda x: len(x) == 6, weekdays))

print(six_letter_list)


""" 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

"""
og_list = ["orange", "red", "green", "blue", "white", "black"]

remove_list = ["orange", "black"]

removed_list = list(
    filter(lambda x: not any(s in x.lower() for s in remove_list), og_list)
)

print(removed_list)

""" 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 """

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [2, 4, 6, 8]

result = list(filter(lambda i: i not in numbers2, numbers))

print(result)

""" 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

"""

og_list = ["red", "black", "white", "green", "orange"]
str1 = "ack"
str2 = "abc"

filt1 = list(filter(lambda x: x.contains(str1), og_list))

print(filt1)


""" 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
"""


""" 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
# based on score
