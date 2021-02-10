#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. `friendly_traceback`
# 2. Review yesterday's content
# 3. Any questions?
# 4. Strings
#    - Searching using `in`
#    - Slices
#    - Immutable strings
#    - Methods
#    - Loops
# 5. Lists
#    - Creating lists
#    - Using lists
#    - Mutable lists (vs. immutable strings)
#    - Lists and strings, and how they're similar (and different)

# In[1]:


x = 100
y = 200

x + z


# In[57]:


from friendly_traceback.ipython import *


# In[3]:


x + z


# In[4]:


explain()


# In[6]:


x = 100

if x == 100:
    print('Equal!')


# In[7]:


x = 100

if x = 100:
    print('Equal!')


# # Recap from Monday
# 
# - To assign to a variable, we use `=`
#     - If the variable already existed, its value is replaced
#     - If the variable didn't previously exist, it is created
# - We have different types of values
#     - `bool` (`True` and `False`)
#     - `int` (integers, whole numbers)
#     - `float` (numbers with a decimal point)
#     - `str` (strings, text)
# - Conditions allow us to make deciisons in our code
#     - `if` looks to its right, and asks: Does that give me a `True` value?
#     - If it's `True`, then we execute the block under the `if`
#     - If not, then we execute the `else` block
#     - (You can have `elif` tests and blocks between those, too.)
# - Comparison operators, which return `True` or `False` (thus useful in `if`)
#     - `==`
#     - `!=`
#     - `<`, `<=`
#     - `>`, `>=`
# - Boolean logical operators
#     - `and`
#     - `or`
#     - `not`
# - Strings
#     - Retrieve from a string using `[]`
#     - Indexes start at 0, and go up to `len(s) - 1` for a string `s`
#     - `len` returns the length of the string
# - Functions for input and output
#     - `print` for printing on the screen
#     - `input` for getting input from the user as a string
# - Conversion
#     - Use the type you *want* as a function
#     - `int('5')` returns the integer 5
#     - `str(5)` returns the string `'5'`

# # Exercise: Birthday calculator
# 
# 1. Ask the user to enter their birth year.
# 2. Ask the user to tell us which birthday we should calculate the year for.
# 3. If the birthday is > 100, then add a hearty congratulations.
# 4. If the birthday is < 0, then scold them a bit for being sarcastic.
# 5. Tell them in what year they'll celebrate that birthday.
# 
# Example:
# 
#     Enter birthyear: 1970
#     Enter birthday: 110
#        Wow, congratulations on reaching 110 years!
#        That will be in 2080
#        
# Hints:
# - We get strings back from `input`, so you'll need to use `int` to turn inputs into numbers.
# - You'll need to use `if` to check the birthdays, if they're very high or very low.

# In[8]:


2+2


# # Strategy and steps
# 
# 1. Ask the user to enter their birth year (`input`), giving us a string, assigning to `birthyear`.
# 2. Ask the user to enter what birthday we should find, into `birthday`.
# 3. Convert them both into integers using `int`.  
# 
# ```python
# x = int(x)  # this means: turn x into an int, and then assign back to x
# ```
# 
# 4. Check: Is the year < 0? Print something
# 5. Check: Is the year > 100? Print something
# 6. Print a report / output, showing in what year they'll have that age.

# In[9]:


birthyear = input('Enter birthyear: ')
birthday = input('Enter birthday: ')

print(f'You were born in {birthyear}, so your {birthday} birthday will be in {birthyear+birthday}!')


# In[10]:


# FUNCTION(DATA)

# to convert a string into an integer
# function: int
# data: the variable containing the string

int(birthyear)  # this returns an integer


# In[11]:


birthyear = input('Enter birthyear: ')
birthday = input('Enter birthday: ')

birthyear = int(birthyear)  # convert birthyear into an int
birthday = int(birthday)  # convert birthday into an int

print(f'You were born in {birthyear}, so your {birthday} birthday will be in {birthyear+birthday}!')


# In[13]:


birthyear = input('Enter birthyear: ')
birthday = input('Enter birthday: ')

birthyear = int(birthyear)  # convert birthyear into an int
birthday = int(birthday)  # convert birthday into an int

if birthday < 0:
    print(f'{birthday} is not a legit birthday!')
    
if birthday > 100:
    print(f'Congrats on reaching your {birthday} birthday!')

print(f'You were born in {birthyear}, so your {birthday} birthday will be in {birthyear+birthday}!')


# In[ ]:


birthyear = input('Enter birthyear: ')
birthday = input('Enter birthday: ')

birthyear = int(birthyear)  # convert birthyear into an int
birthday = int(birthday)  # convert birthday into an int

if birthday < 0:
    print(f'{birthday} is not a legit birthday!')
    
else:
    if birthday > 100:
        print(f'Congrats on reaching your {birthday} birthday!')

    print(f'You were born in {birthyear}, so your {birthday} birthday will be in {birthyear+birthday}!')


# In[14]:


s = 'abcdefghijklmnopqrstuvwxyz'
len(s)


# In[15]:


# I can retrieve characters with [] and an index, starting with 0

s[2]


# In[16]:


s[10]  # k is the 11th letter, but since we start counting with 0, s[10] is 'k'


# In[17]:


s


# In[18]:


s[0] = '!'


# # Strings are immutable
# 
# - You can never change a string once it's created.
# - You *CAN* assign a new string to a variable.
# - You *CAN* create a new string based on an old one

# In[19]:


s = 'abcde'
s = 'fghij'


# In[20]:


# We can search in strings using "in"

s = 'abcdefghijklmnopqrstuvwxyz'
'j' in s  # returns True or False


# In[22]:


'f' in s


# In[23]:


'abcd' in s


# In[25]:


'abd' in s


# In[26]:


# slices -- Python's version of "substrings"

s


# In[27]:


s[5] # retrieve the item at index 5


# In[28]:


s[5:10]  # retrieve the "slice" starting at index 5, until (not including) index 10


# In[29]:


s[2:20]


# In[30]:


s[:15]  # from the start of s until (not including) index 15


# In[31]:


s[15:]  # from index 15 through the end


# In[32]:


s[5]+ s[10:15] + s[2]


# In[33]:


if 'a' in 'abcd':
    print('Yes!')


# # Exercise: Pig Latin translator
# 
# To translate from English into Pig Latin:
# 
# 1. Check the first letter of the English word.
# 2. If the first letter is a vowel (a, e, i, o, or u) then add `way` to the end of the word.
# 2. In other cases, move the first letter to the end, and then add `ay`.
# 
# Some examples:
# - `computer` -> `omputercay`
# - `apple` -> `appleway`
# - `elephant` -> `elephantway`
# - `octopus` -> `octopusway`
# - `table` -> `abletay`
# - `papaya` -> `apayapay`
# 
# 1. Ask the user to enter an English word (all lowercase, no punctuation, no spaces)
# 2. Check the first letter.  Is it a vowel?
#     - One way: use `or` in an `if` statement
#     - Another way... consider `in`
# 3. Use `if` to decide what rule applies
# 4. Adding to a string is as easy as `+` or an f-string
# 5. Moving the first letter to the end means using slices and creating a new string
# 
# 

# In[34]:


s = 'abcde'

if s[0] == 'a'  or s[0] == 'e':
    print('It starts with a vowel!')


# In[35]:


if s[0] in 'aeiou':  # standard Python practice!
    print('It starts with a vowel!')
    


# In[37]:


word = input('Enter a word: ')

if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
    print(word + 'way')


# In[39]:


# Never do this!  It thinks that *all* words start with vowels!
if word[0] == 'a' or 'e' or 'i' or 'o' or 'u':
    print(word + 'way')


# In[40]:


word = input('Enter a word: ')

# syntax of "in" is always: LITTLE in BIG, and returns True/False

if word[0] in 'aeiou':
    print(word + 'way')
else:
    print(word[1:])  # everything but the first letter
    print(word[0])   # just the first letter
    print('ay')


# In[41]:


word = input('Enter a word: ')

# syntax of "in" is always: LITTLE in BIG, and returns True/False

if word[0] in 'aeiou':
    print(word + 'way')
else:
    print(word[1:] + word[0] + 'ay')


# In[42]:


word = input('Enter a word: ')

# syntax of "in" is always: LITTLE in BIG, and returns True/False

if word[0] in 'aeiou':
    print(word + 'way')
else:
    print(f'{word[1:]}{word[0]}ay')


# # Next up:
# 
# - Methods (alternative syntax for functions)
# - Loops (repeating yourself without repeating yourself)

# In[43]:


s


# In[44]:


len(s)


# # Functions vs. methods
# 
# Both functions and methods are verbs, actions you can take on data.
# 
# Functions are free-floating in Python's memory, always available. 
# 
# Examples:
# 
# ```python
# len(s)           # call the "len" function on the string "s"
# print('hello')   # call the "print" function on the string 'hello'
# input('Age: ')   # call the "input" function on the string 'Age:'
# ```
# 
# Syntax for functions will always be
# 
#     FUNCTION(DATA)
# 
# Methods, by contrast, are attached to an object.  They always have the syntax of:
# 
#     DATA.METHOD() 
#     
# You can also pass additional arguments:
# 
#     DATA.METHOD(ARG1, ARG2)
#     
# Examples of methods:
# 
# ```python
# s = 'aBcDeF'
# s.upper()  # string method, returns a new string, uppercase of s, or 'ABCDEF'
# s.lower()  # string method, returns a new string, lowercase of s, or 'abcdef'
# s.capitalize()  # string method, return a new string -- all lowercase but caps 1st letter
# ```

# In[49]:


s = 'aBcDeF'


# In[50]:


s.upper()


# In[51]:


s.lower()


# In[52]:


s.capitalize()


# In[53]:


# What methods exist?  What else can I do?


# In[54]:


# Best place to look: Python documentation

# Example of a useful string method: isdigit

# s.isdigit() returns True if all characters in s are digits
#  (and thus, s can be turned into an integer)


# In[55]:


int('5')


# In[56]:


int('abcd')


# In[57]:


'5'.isdigit()


# In[58]:


'abcd'.isdigit()


# # When learning a method, ask:
# 
# 1. What type does it work on?
# 2. What arguments (if any) does it need, beyond the object itself?
# 3. What does it return?
# 4. Does it modify anything?

# # Exercise: Add two numbers... if you can
# 
# 1. Ask the user to enter two numbers, each of which will be assigned to a different variable (`first` and `second`).
# 2. If both inputs can be turned into numbers and added, do so, and print the result.
# 3. If one or both cannot be turned into an integer, then scold the user.
# 
# Example:
# 
#     Enter first number: 2
#     Enter second number: 3
#     2 + 3 = 5
#     
#     Enter first number: abcd
#     Enter second number: 3
#     abcd is not a number
#     
#     Enter first number: 2
#     Enter second number: abcd
#     abcd is not a number
#     
# Hints and notes:
# 
# 1. Remember to use the `int` function (not a method!) to get an integer from a string.
# 2. Use the `.isdigit` method (not a function, runs on strings only), to make sure that you can safely turn a string into an integer.
# 3. You can use `if`, `elif`, and `else`
# 4. You might well need to use `not`, which reverses the truth of whatever is to its right (including the result of a method call... hint, hint)
# 

# In[1]:


s = 1234
s.upper()


# In[2]:


s = 'xyz'
s.upper()


# In[3]:


x = '1234'   # the variable x now contains the string '1234'

x.isdigit()  # returns True, because the string that x refers to is only 0-9


# In[4]:


'x'.isdigit()  # does the string 'x' contain only the digits 0-9?  False


# In[5]:


s = input('Enter a number: ')


# In[7]:


s.isdigit()  # isdigit runs on strings, so this works


# In[8]:


s = int(s)
s.isdigit()   # this will NOT WORK, because we've already changed so to be an int!


# In[9]:


# the reason we're going to use .isdigit() is to check whether it's safe
# to turn our string into an integer

# so *FIRST* use isdigit to check
# THEN, if it's safe, convert


# In[20]:


first = input('Enter first: ')
second = input('Enter second: ')

if first.isdigit() and second.isdigit():
    first = int(first)
    second = int(second)
    print(f'{first} + {second} = {first+second}')
else:
    if not first.isdigit():
        print(f'{first} is not numeric')
        
    if not second.isdigit():
        print(f'{second} is not numeric')


# In[22]:


name = input('Enter your name: ')
print(f'Hello, {name}!')


# In[23]:


name


# In[24]:


# the "strip" method removes whitespace from the outside of a string
# and returns a new string without it

name


# In[25]:


name.strip()  # returns a new string


# In[26]:


name


# In[27]:


s = ' 123 '
s.isdigit()


# In[28]:


name = input('Enter your name: ')
name = name.strip()  
print(f'Hello, {name}!')


# In[29]:


name


# In[ ]:


# Very common idiom in Python for getting input

name = input('Enter your name: ').strip()
print(f'Hello, {name}!')


# # Loops

# In[30]:


s = 'hello'

print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])


# In[31]:


# DRY -- don't repeat yourself


# In[32]:


# "for" loop

for one_character in s:
    print(one_character)


# In[33]:


for one_very_long_novel in s:
    print(one_very_long_novel)


# # Exercise: vowels, digits, and others
# 
# 1. Define three variables, `vowels`, `digits`, and `others`, all to be 0.
# 2. Ask the user to enter a string.
# 2. Go through each character in the string.
#     - If the current character is a vowel, add 1 to `vowels`
#     - If the current character is a digit, add 1 to `digits`
#     - If the current character is neither, add 1 to `others`
# 3. Print each of the counters and their current values.    

# In[ ]:


s = input('Enter a string: ').strip()

for one_character in s:
    # if...  one_character a vowel?

    # elif ... is one_character a digit?

    # else...
    


# In[ ]:


x = 100
x += 1   # this adds 1 to the variable x


# In[36]:


# Setup
vowels = 0
digits = 0
others = 0

# Calculation
s = input('Enter a string: ').strip()

for one_character in s:
    if one_character in 'aeiou':
        print(f'{one_character} is a vowel')
        vowels += 1
    elif one_character.isdigit():
        print(f'{one_character} is a digit')
        digits += 1
    else:
        print(f'{one_character} is something else')
        others += 1

# Report    
print(f'vowels = {vowels}')
print(f'digits = {digits}')
print(f'others = {others}')


# In[37]:


print('Yay!')
print('Yay!')
print('Yay!')


# In[39]:


for counter in range(3):
    print('Yay!')


# In[40]:


total = 0

times_to_ask = input('How many numbers? ').strip()
times_to_ask = int(times_to_ask)

for counter in range(times_to_ask):
    n = input(f'{counter} Enter a number: ').strip()
    if n.isdigit():
        total += int(n)
        
    else:
        print(f'{n} is not numeric')
        
print(f'total = {total}')


# # Two different ways to use `for` loops
# 
# - Iterate over a string. We get, in each iteration, one character from the string.
# - Iterate over `range(n)`, where `n` is an integer. We get, in each iteration, an integer, starting with 0 up to and not including `n`.

# # `while` loops
# 
# `while` loops work just like `if` statements, except that the body of the loop runs as many times as necessary, until the condition returns `False`.

# In[41]:


x = 5

if x > 0:
    print(f'x = {x}')
    x -= 1  # remove 1 from x
    
print(f'x = {x}')


# In[42]:


x = 5

while x > 0:  # so long as this is true, repeat this block of code
    print(f'x = {x}')
    x -= 1  # remove 1 from x
    
print(f'x = {x}')


# # Infinite loops

# In[43]:


while True:
    name = input('Enter your name: ').strip()
    
    if name == '':   # The empty string?  Get out of the loop!
        break   
        
    print(f'Hello, {name}!')


# In[44]:


while True:
    name = input('Enter your name: ')
    
    if name == '':   # The empty string?  Get out of the loop!
        break   
        
    print(f'Hello, {name}!')


# # Exercise: Sum numbers
# 
# 1. Assign `total` the value 0.
# 2. Use an infinite loop (i.e., `while True`) to ask the user to enter a string.
#     - If we get an empty string, break from the loop and print the total
#     - If we get something numeric (i.e., `isdigit`), then turn into a number and add to `total`
#     - If we get something non-numeric (i.e., `not isdigit`), then scold the user and go back.
#     
# Example:
# 
#     Enter a number: 10
#     Enter a number: 20
#     Enter a number: abcde
#         abcde is not a number!
#     Enter a number: 30
#     Enter a number: [ENTER]
#     Total is 60

# In[46]:


total = 0

while True:
    s = input('Enter a number: ').strip()
    
    if s == '':
        break     # did we get empty input from the user? Leave the "while" loop!
        
    if s.isdigit():
        total += int(s)
        
    else:
        print(f'{s} is not numeric')
        
print(f'total = {total}')


# # What can we do with strings?
# 
# 1. Retrieve one element with `[i]`, where `i` is an index
#     - First element is at index 0
#     - Final element is at index `len(s) - 1`
# 2. Get the length with `len(s)`
# 3. Get a slice using the syntax `[start:end]`
# 4. Search in a string using `in`
# 5. Iterate over the string using a `for` loop
# 6. Many string methods

# # Data structure: Lists
# 
# A list is a container for other objects. It can contain any number of other objects, and of any type.  You can even mix types of objects within a list, although it's traditional not to do this.

# In[47]:


# Create a list using []

# empty list
mylist = []

# list with integers
mylist = [10, 20, 30]   # commas between elements

# list of strings
mylist = ['abcd', 'efghi', 'jk']


# In[48]:


mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# In[49]:


# 1. Retrieve one element with `[i]`, where `i` is an index
#     - First element is at index 0
#     - Final element is at index `len(s) - 1`

mylist[0]


# In[50]:


mylist[5]


# In[51]:


mylist[len(mylist) - 1]


# In[52]:


mylist[-1]


# In[53]:


# 2. Get the length with `len(s)`
len(mylist)


# In[54]:


# 3. Get a slice using the syntax `[start:end]`
mylist[2:8]  # from index 2 until (not including) index 8


# In[55]:


# 4. Search in a string using `in`
40 in mylist


# In[56]:


# 5. Iterate over the string using a `for` loop
for one_item in mylist:
    print(one_item)


# # Exercise: Basic list retrieval
# 
# 1. Define a list containing 10 integers.
# 2. Ask the user to enter two integers, called `first_i` and `second_i`.
# 3. Retrieve the elements at indexes `first_i` and `second_i`, and add them.
# 4. Print the entire expression, including the sum.
# 
# Example:
# 
#     Enter first index: 3
#     Enter second index: 5
# 
#     At index 3, we have 40
#     At index 5, we have 60
# 
#     40 + 60 = 100

# # Strategy
# 
# 1. Create a list.  You'll always have square brackets (`[ ]`), and as many elements as you want, separated by commas.  You'll need to assign it to a variable.
# 2. Use `input` to assign values to `first_i` and `second_i`.
#     - These will be strings
#     - Use `int` to convert them
#     - You can check if they're int-able, but don't worry too much.
# 3. Use these two variables (`first_i` and `second_i`) to retrieve items from the list
#     - You can retrieve from the list using `mylist[first_i]` and `mylist[second_i]`
#     - Put these retrieved numbers into variables
# 4. Use an f-string to print them out
# 

# In[58]:


[10, 20 30, 40]


# In[ ]:


my_list = [10,10,20,20,30,40]

first_index = input("Enter first index: ")
first_index = int(first_index)+1

second_index = input("Enter Second index: ")
second_index = int(second_index)+1

l_my_list = len(my_list) + 1

if l_my_list >= first_index and l_my_list >= second_index:
    for i in my_list:
        print(i[first_index])
        print(i[second_index])
        #print(f'{i[first_index]+i[second_index]}')
else:
    print("index valuue is out of value")


# In[59]:


#         0   1  2  3  4  5
mylist = [10,10,20,20,30,40]

mylist[3]   # give me the element at index 3


# In[60]:


mylist[5]


# # Where is there a difference of 1?
# 
# 1. Between the max index and the length. `len(thing)` will always be 1 more than the highest index of `thing`.
#     - The string `abcde` has a max index of 4, but a len of 5.
#     - The list `[10, 30, 30]` has a max index of 2, but a len of 3.
# 2. Also, in slices -- the end index is 1 more than we actually get.
#     - In the string `abcde`, the slice `[1:3]` will be from index 1 until (and not including) index 3, which means `bc`.

# In[62]:


#         0   1  2  3  4  5
mylist = [10,10,20,20,30,40]

first_i = input("Enter first index: ")
first_i = int(first_i)

second_i = input("Enter Second index: ")
second_i = int(second_i)

first_value = mylist[first_i]
second_value = mylist[second_i]

total = first_value + second_value

print(f'{first_value} + {second_value} = {total}')


# In[63]:


mylist = [10, 20, 30]
len(mylist)


# In[64]:


mylist[2]


# In[65]:


# I can add new elements to a list, too!
# I can also modify existing list elements
# Because lists are MUTABLE -- they can be changed!

mylist


# In[66]:


mylist[0] = 9999
mylist


# In[67]:


mylist.append(40)  # this adds 40 to the end of mylist
mylist


# In[68]:


mylist.append(50)
mylist


# In[69]:


mylist.append('abcde')
mylist


# In[70]:


mylist.append([100, 200, 300])
mylist


# In[71]:


# the modulus operator, %
# it means: divide, and return the remainder

10 % 2 #  == 0


# In[72]:


15 % 4  # 15/4, what's the remainder?


# In[73]:


20 % 9  # 20 / 9, what's the remainder?


# In[74]:


# if I want to know whether a number is even or odd, 
# I can use % 2

10 % 2  # this is 0, so it's even


# In[75]:


11 % 2   # this is 1, so it's odd


# In[ ]:





# # Exercise: evens and odds
# 
# 1. Define two empty lists, `evens` and `odds`.
# 2. Ask the user repeatedly (in a `while True` loop) to enter a number, and store it in `s`.
#     - If you get an empty string (`if s == ''`), stop asking -- `break` from the loop
#     - If you get something for which `s.isdigit()` returns `True`, then 
#         - turn it into an integer with `int()` 
#         - check if it's even or odd
#             - If it's even, append to `evens`
#             - If it's odd, append to `odds`
#     - If you get a non-number, scold the user
# 3. Print `evens` and `odds`
# 
# Example:
# 
#       Enter a number: 10
#       Enter a number: 11
#       Enter a number: abcd
#           Not a number!
#       Enter a number: 15
#       Enter a number: [ENTER]
#       
#       evens: [10]
#       odds: [11, 15]

# In[83]:


# setup
evens = []
odds = []

# calculation
while True:

    s = input('Enter a number: ').strip()

    if s == '':   # if we got an empty string, stop asking
        break
    
    if s.isdigit():
        s = int(s)

        if s % 2 == 1:    # if it's odd, add to "odds"
            odds.append(s)
        else:             # if it's even, add to "evens"
            evens.append(s)

    else:
        print(f'{s} is not numeric')

# report
print(f'odds = {odds}')
print(f'evens = {evens}')


# In[80]:


evens


# In[81]:


odds


# # Exercise: Short vs. long words
# 
# For the purposes of this exercise, we'll define a short word as having 4 letters or fewer. Long words have more than 4 letters.
# 
# 1. Create two lists, `long_words` and `short_words`.  These are empty lists.
# 2. Define a string, `s`, based on user input.
# 3. Get its length (with `len`) and then print whether it's a short word or a long word, based our definition.

# In[85]:


long_words = []
short_words = []

s = input('Enter a word: ').strip()

if len(s) <= 4:
    print('Short!')
else:
    print('Long!')


# # Exercise: Short vs. long words (part 2)
# 
# For the purposes of this exercise, we'll define a short word as having 4 letters or fewer. Long words have more than 4 letters.
# 
# 1. Create two lists, `long_words` and `short_words`.  These are empty lists.
# 2. Define a string, `s`, based on user input.
# 3. Get its length (with `len`), and use that information to add the word to the appropriate list, either `long_words` or `short_words`.  Remember you can use the `append` method to add to the appropriate list.
# 4. Print both lists.  (And yes, only one will have anything in it, a single word.)

# In[ ]:


short_words = []
long_words = []

s = input('Enter a word: ').strip()

if len(s) <= 4:
    short_words.append(s)
else:
    long_words.append(s)
    
print(f'short_words = {short_words}')
print(f'long_words = {long_words}')


# # Exercise: Short vs. long words (part 3)
# 
# For the purposes of this exercise, we'll define a short word as having 4 letters or fewer. Long words have more than 4 letters.
# 
# 1. Create two lists, `long_words` and `short_words`.  These are empty lists.
# 2. Use a `while True` loop to ask for user input repeatedly.
# 3. If the user gives us an empty string, then exit the loop.
# 4. Otherwise, get the word's length (with `len`), and use that information to add the word to the appropriate list, either `long_words` or `short_words`.  Remember you can use the `append` method to add to the appropriate list.
# 5. Print both lists. Between the two lists, you will see all of the words that you entered.

# In[3]:


short_words = []
long_words = []

while True:
    s = input('Enter a word: ').strip()
    
    if s == '':
        break

    if len(s) <= 4:
        short_words.append(s)
    else:
        long_words.append(s)
    
print(f'short_words = {short_words}')
print(f'long_words = {long_words}')


# In[5]:


short_words = []
long_words = []

while True:
    s = input('Enter a word: ').strip()

    if len(s) <= 4:
        short_words.append(s)
    else:
        long_words.append(s)
        
    if s == '':
        break        
    
print(f'short_words = {short_words}')
print(f'long_words = {long_words}')


# In[6]:


s = '5'
int(s)  # returns a new int, based on s


# In[7]:


n = 5
str(s)  # returns a new str, based on n


# In[8]:


s = 'abcde'
# how can I turn this into a list?

list(s)


# In[9]:


s = 'abcd efgh ijkl'
list(s)


# In[10]:


# to turn a string into a list of strings, we can use the "split" method
# don't confuse "strip" and 'split"

# str.split is run on a string, and takes an argument -- what should be used to split
# we get back a list of strings, which were separated by the argument

s


# In[11]:


s.split(' ')   # use space as the separator between elements


# In[12]:


s.split('e')  # use 'e' as the delimiter


# In[13]:


s = 'abcd   ef    ghij   kl'
s.split(' ')  # use space as a delimiter


# In[14]:


# the solution is: don't pass an argument.
# that means: use any whitespace, any length
s.split() 


# In[15]:


s = 'abcd:efgh:ijkl:mn'

s.split(':')


# # Tomorrow
# 
# 1. Talk more about `str.split` and `str.join`
# 2. Dictionaries (aka key-value stores, hash tables)
# 3. Files (reading from, writing to text files)
# 4. Install PyCharm, so we can write code on our own computers
#     - For homework, please download and install Python and PyCharm
#     - Python: https://python.org/
#     - PyCharm: https://www.jetbrains.com/pycharm/download/

# In[ ]:




