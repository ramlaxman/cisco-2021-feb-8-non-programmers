#!/usr/bin/env python
# coding: utf-8

# In[4]:


print('Hello, world!!!!')   # shift+enter == run the code in the current cell


# # Exercise: Getting started with Jupyter
# 
# 1. Go to my Jupyter server at http://python.lerner.co.il:8000/
# 2. On that Jupyter home page, use the "New" menu on the right side to start a new notebook.
# 3. When the new notebook opens, click on the title and change it to be your name and the date.
# 4. In a cell, use the `print` function to print some text.  Text can be between single quotes ('') or double quotes("") — Python doesn't care, so long as they match.

# When you're done with the exercise, click the green check mark (bottom left of the "participants" panel) to let me know.

# # Agenda
# 
# 1. Basics
#     - Variables
#     - Different types are different
#     - Conditions with `if` / `else`
# 2. Data structures
#     - Numbers (integers and floats)
#     - Strings (text)
#     - Loops -- repeating yourself in code
#     - Lists and tuples
#     - Dictionaries
#     - Files (reading from and writing to text files)
# 3. Functions
#     - Here, we'll start writing in an IDE (PyCharm)
# 4. Modules
#     
# 

# In[1]:


print('abcd')   # pressing ENTER goes down one line
print('efgh')   # pressing ENTER goes down one (another!) line
print('ijkl')   # pressing shift + ENTER executes the entire cell


# In[2]:


print(2)


# In[3]:


print(2 + 5)


# In[4]:


print(3 * 4)  # in programming, we use * for multiplication


# In[5]:


print(2 + 3 * 4)  # Python knows the order of operations


# In[6]:


# In programming, we have pronouns!
# they are known as "variables"

# Variables have names, and those names DO NOT have quotes around them
# I can assign to a variable (i.e., give it a value with the = sign)

x = 5    # assigns 5 to the variable x... and since x didn't exist before, now it does!
y = 3    # assigning 3 to the variable y... it's created, too!

print(x + y)


# In[7]:


name = 'Reuven'

print('Hello, ' + name)


# In[8]:


name + name


# In[9]:


x + name   


# # Exercise: Greeting yourself
# 
# 1. Assign your name (a text string) to the variable `name`.
# 2. Print a greeting to yourself.
# 3. How can you print a greeting that ends with a `.`?

# In[ ]:


# the = sign in Python means: Assign the value on the right to the name on the left
the_variable_name = 'the variable value'


# In[10]:


a = 100
b = 2345

print(a + b)


# In[11]:


a = 999
b = 888

a + b


# In[12]:


name = 'Reuven'
print('Hello, ' + name)


# In[13]:


print('Hello,' + name)


# In[14]:


print('Hello, ' + name + '.')


# # Variable names
# 
# They can contain any combination of:
# 
# - Letters (uppercase and lowercase are *different*)
# - Numbers
# - Underscores (`_`)
# 
# But:
# 
# - The name must start with a letter or underscore
# - It's traditional only to use lowercase letters
# - If the name starts with an underscore, Python sees it as "private," not for others to use

# In[ ]:





# In[17]:


name = 'Reuven'
favorite_number = 72

# f-strings (format strings) to the rescue!
# they allow us to mix and match any data type when creating a string

# Put an f before the opening quote, and {} suddenly are replaced with their values
print(f'Hello, {name}, with a favorite number {favorite_number}!')


# # Exercise: Another greeting (with f-strings)
# 
# 1. Define a variable, `name`, with the text string of your name.
# 2. Define another variable, `birthyear`, to be the year in which you were born.
# 3. Define a third variable, `age_this_year`, to be how old you'll turn this year, calculated based on `birthyear`.
# 4. Print a message to the user, saying how old they'll turn this year.  Use an f-string to do this.

# In[18]:


x = 100
y = 50

print(x + y)


# In[19]:


print(x - y)


# In[20]:


z = x - y  # defines z to be a variable, whose value is the result of x-y


# In[21]:


print(z)


# In[22]:


name = 'Reuven'
birthyear = 1970
age_this_year = 2021 - birthyear
print(f'Hello, {name}.  You will turn {age_this_year} this year!')


# In[23]:


x = '10'  # string!
y = '20'  # string!

x + y


# In[24]:


x - y


# In[26]:


x = 10   # no quotes -- numbers
y = 20  #  no quotes -- numbers

x + y  # in Jupyter, the final line of a cell, if it returns a value, shows it on the screen


# In[27]:


x


# In[28]:


y


# In[29]:


x*y


# In[ ]:





# # The `input` function
# 
# Just as the `print` function displays something on the screen, the `input` function asks the user to give it input.  Whatever the user typed is returned by the function as a string.
# 
# 

# In[32]:


# in assignment (=), the right side runs before the left side

s = input('Enter your name: ')   


# In[33]:


print(s)


# In[34]:


s+s  # adding a string to itself -- we get s+s, not the numeric s+s


# # Exercise: Greetings, with feeling!
# 
# 1. Ask the user to enter their name, and assign this to `name`.
# 2. Ask the user to enter their current emotional state, to the variable `feeling`.
# 3. Print a greeting to the user acknowledging their feelings.

# In[35]:


name = input('Enter your name: ')
feeling = input('How are you feeling? ')

print(f'Hey, {name}, good to know you are feeling {feeling}.')


# # Conditionals — Making decisions
# 
# - If I want to assign a value to a variable, I use `=`, the assignment operator.
# - If I want to compare two things, I use `==`, the comparison operator.

# In[37]:


name = input('Enter your name: ')

if name == 'Reuven':    # if this comparison returns True, then we execute if's body/block
    print('Hello, boss!')
    print('Nice to see you again!')
else:
    print(f'Hello, {name}.  Nice to meet you!')


# # Exercise: Where do you work?
# 
# 1. Ask the user where they work, and assign to a variable named `company`.
# 2. If the user also works at Cisco, give them a warm greeting.
# 3. If not, then give them an appropriately snarky response.

# In[41]:


company = input('Enter your company: ')

if company == 'Cisco':
    print('Wow! I must be your colleague!')
else:
    print('Well, I am sure you are sorta kinda happy where you work.')


# In[43]:


# the logical way, with what we know

color = input('Enter your favorite color: ')

if color == 'red':
    print('Good to know you like red.')
    
else:
    if color == 'blue':
        print('I like blue, too')
    else:
        print('I guess you like something that is neither red nor blue')


# In[44]:


# the better way

color = input('Enter your favorite color: ')

if color == 'red':
    print('Good to know you like red.')
    
elif color == 'blue':
    print('I like blue, too')

else:
    print('I guess you like something that is neither red nor blue')


# In[45]:


# the better way

color = input('Enter your favorite color: ')

if color == 'red':
    print('Good to know you like red.')
    
elif color == 'blue':
    print('I like blue, too')
    
elif color == 'green':
    print('It is a great color!')

else:
    print('I guess you like something that is neither red nor blue')


# In[46]:


# the better way

color = input('Enter your favorite color: ')

if color == 'red':
    print('Good to know you like red.')
    
elif color == 'blue':
    print('I like blue, too')
    
elif color == 'green':
    print('It is a great color!')
    
elif color == 'blue':
    print('EVIL SECOND BLUE MATCH!')

else:
    print('I guess you like something that is neither red nor blue')


# # Exercise: Current and former company
# 
# 1. Ask the user where they worked.
# 2. If they work at Cisco, then congratulate them on being a colleague.
# 3. If they worked at your previous job, then say you *used* to be their colleague.
# 4. Otherwise, say something snarky.

# In[49]:


company = input('Where do you work? ')

if company == 'Cisco':
    print('You work at Cisco, too? Wow! We are colleagues!')
elif company == 'Time Warner':
    print('I used to work there... once upon a time...')
else:
    print(f'I have never heard of that sad company, {company}.')


# In[52]:


s = 'Hi, I\'m Reuven'   # \' means that the ' is not ending/starting the string, but literal
print(s)


# In[53]:


s


# # Boolean logic
# 
# - X and Y are true: We represent in Python with `and`
# - X or Y is true: We represent in Python with `or`
# - not X: We represent in Python with `not`

# In[54]:


x = True
y = True

x and y  # if both the left and right sides are True, this returns True


# In[55]:


if x and y:
    print('Both x and y are True!')


# In[56]:


x = 10
y = 20

x == 10 and y == 20


# In[57]:


x == 55 and y == 20


# In[59]:


x = 10
y = 20

x == 10 or y == 55  # one value is True, so the entire "or" expression is True


# In[60]:


x == 999 or y == 20  # one value is True, so the entire "or" expression is True


# In[61]:


if x == 999 or y == 20:
    print('One of them is what you want')


# In[62]:


not True


# In[63]:


not False


# In[65]:


x = 10

if not x == 20:
    print('x is not 20')


# In[66]:


if (x == 999) or (y == 20):
    print('One of them is what you want')


# In[68]:


# If we put parentheses around an expression, we have much more flexibility regarding
# new lines and indentation

if (x == 999 or    # Now we can use more than one line!
    y == 20):
    print('One of them is what you want')


# In[69]:


# If we put parentheses around an expression, we have much more flexibility regarding
# new lines and indentation

if (x == 999 or    # Now we can use more than one line!
    y == 20 or
    y == 25 or
    y == 'abcd'):
    print('One of them is what you want')


# # Exercise: Name and company
# 
# 1. Ask the user to enter their name, and assign it to a variable, `name`.
# 2. Ask the user to enter their company, and assign it to a variable, `company`.
# 3. If the name and company are the same, then say it must be you!
# 4. If the name is the same (but not the company), say they have your name at a rival.
# 5. If the company is the same (but not the name), then say you're colleagues.
# 6. If neither is the same, say something snarky.

# # Strategy
# 
# 1. Ask two questions, and assign to two variables (`name` and `company`)
# 2. Four different possibilities:
#     - Both `name` and `company` match what we want (`and`) 
#     - `name` matches, but `company` doesn't (just have to check if `name` matches)
#     - `company` matches, but `name` doesn't (just have to check if `company` matches)
#     - `else` can be if neither matches
#     

# In[71]:


name = input('Enter your name: ')
company = input('Enter your company: ')

if name == 'Reuven' and company == 'Cisco':
    print('Hey, you must be me!')
    
elif name == 'Reuven':   # implicitly, company is not 'Cisco'
    print('You have my name, but work for a competitor!')

elif company == 'Cisco':   # implicitly, name is not 'Reuven'
    print('You are my colleague, but have another name')
    
else:
    print(f'Oh, you work at {company}? Oh, well.')


# # Comparison operators
# 
# All of these take two arguments (one on the left, one on the right) and return `True` or `False`. So we can use them in an `if` statement, but we can also string them together inside of a larger, more complex logical condition with `and`, `or`, and `not`:
# 
# - `==` # are these things equal?  a == b
# - `!=` # are these things unequal?   a != b 
# - `<`  # less than
# - `<=` # less than or equal
# - `>`  # greater than
# - `>=` # greater than or equal

# In[72]:


10 < 5


# In[73]:


5 < 10


# In[75]:


'hello' < 'goodbye'  # with text strings, < and > work alphabetically


# In[76]:


'ab' < 'abc'


# In[77]:


'goodbye' < 'hello'


# # Exercise: Which word comes first?
# 
# 1. Ask the user to enter two words, and assign them into two variables, `first` and `second`.
# 2. Use `if`/`elif`/`else` to tell us:
#     - `first` and `second` are the same
#     - `first` comes before `second` alphabetically
#     - `second` comes before `first` alphabetically
#     
# Only use lowercase letters! (Or if you finish, and want to amuse yourself, use them!)

# # Strategy
# 
# 1. Ask the user to enter a value for `first`
# 2. Ask the user to enter a value for `second`
# 3. Consider:
#     - Does `first` come before `second`?  (Compare them with `<`)
#     - Does `second` come before `first`? (Compare with `<`)
#     - If neither of the above is true, then we can assume they're equal.

# In[80]:


first = input('Enter first word: ')
second = input('Enter second word: ')

if first < second:
    print(f'{first} comes before {second} in the dictionary')
elif first > second:
    print(f'{second} comes before {first} in the dictionary')
else:
    print(f'{first} and {second} are the same!')


# In[81]:


x = 10

if x < 50:
    print(f'{x} is less than 50')
    
if x < 100:
    print(f'{x} is less than 100')
    
if x < 1000:
    print(f'{x} is less than 1000')
    


# In[82]:


x = 10
y = '20'

x + y


# # Data structures
# - `True` and `False`
# - `int` and `float`
# - `str` (strings)
# - `list` (and `tuple`)
# - `dict` (dictionaries)
# - files -- reading froma and writing to
# 

# # Why do we need data structures?

# In[83]:


2 + 3


# # Everything in Python has a type!
# 
# Every single piece of data has a "type," meaning a data structure "class" that describes its capabilities.  Once you know what type of data you have, you know what that data can do.

# In[84]:


s = 'abcd'
t = 'efgh'

s + t


# In[85]:


# You can always find out the type of some data by running the "type" function on it
type(s)


# In[86]:


type(t)


# In[87]:


type(3)


# In[88]:


type(3.5)


# # Data structure: Booleans (`bool`)
# 
# ### Values are `True` and `False` (yes, capitalized)

# In[90]:


s = True

if s == True:   # don't do this!
    print('Yes, s is True!')


# In[91]:


if s:   # if looks to its right, sees s, which is True, and its block runs
    print('Yes, s is True!')


# In[92]:


x = 10

if x == 10:
    print(f'Yes, x is 10!')


# # Data structure: Integers (`int`)
# 
# Integers are whole numbers, so any number you can imagine that doesn't have a fractional part (i.e., doesn't have a decimal point) is an integer.
# 
# 

# In[93]:


x = 100
y = 345

type(x)


# In[94]:


type(y)


# In[95]:


x + y


# In[96]:


x = 10
y = 3


# In[97]:


x + y


# In[98]:


x - y


# In[99]:


x * y   # multiplication 


# In[100]:


x / y   # division - it always returns a float!


# In[101]:


x ** y   # exponentiation


# In[102]:


x % y    # x modulo y, meaning: what's the remainder after running x / y ?


# In[104]:


x = 10
 
# to add 1 to x, we can say:
x = x + 1   # this is assignment!  First calculate the right side, then assign to x


# In[105]:


x


# In[106]:


# We can shrink that to say:

x += 1    # this means: x = x + 1


# In[107]:


x


# In[108]:


x++


# In[109]:


x = input('Enter a number: ')
y = input('Enter another number: ')

print(f'{x} + {y} = {x+y}')


# In[110]:


# How can we turn a string into an integer?
# Use the "int" function on a string; it'll return an int based on that string

int(x) + int(y)


# In[111]:


# int doesn't change x or y -- it returns a new value, which we can use.

# Of course, I could say:

x = int(x)
y = int(y)

x + y


# In[112]:


int('10')


# In[113]:


int('abcde')


# In[114]:


x = 10

if x == 10:  # --> if True:
    print('Yes, it\'s 10!')  # this runs if the conditional expression evaluated to True

else:
    print('No, it is not')   # this runs if the conditional expression evaluated to False


# # Exercise: Number guessing game
# 
# 1. Generate a random integer between 0 and 100 (I'll show you how), and store it in the variable `number`.
# 
# ```python
# import random
# number = random.randint(0, 100)
# ```
# 
# 2. Print the number, so that guessing is much easier.
# 3. Ask the user to guess the number.
#     - Don't forget that `input` returns a string!  You'll need to convert it!
# 4. Print one of:
#     - Too low!
#     - Too high!
#     - You got it!
#     
# Example:
# 
#     Random number is 56
#     Guess: 100
#     Too high!
# 
#     Random number is 28
#     Guess: 3
#     Too low!
#     
#     Random number is 28
#     Guess: 28
#     You got it!
#     
#     
# 
# 

# # Strategy
# 
# 1. Generate a random number
# 
# ```python
# import random
# number = random.randint(0, 100)
# ```
# 
# 2. Print the number
#     - Use an f-string to do that!
#     
# 3. Ask the user to enter a guess.  
#     - Use `input` to get the user's guess
#     - Assign the user's guess to a variable `guess`
#     - That's a string... so use `int` to turn it into an integer
#     - Remember that `int` *RETURNS* an integer.  It doesn't convert it.
# 
# 4. Use `if`/`elif`/`else` to determine whether `guess` is larger than `number`, smaller than `number`, or the same.
# 

# In[121]:


import random
number = random.randint(0, 100)

print(f'number = {number}')

guess = input('Enter a guess: ')


# In[124]:


# is the integer 82 equal to the string '82'?  NO IT IS NOT!
guess == 82


# In[125]:


# create an integer based on the string "guess",
# and then assign it to the variable "guess"
guess = int(guess)   

type(guess)


# In[129]:


import random
number = random.randint(0, 100)

print(f'number = {number}')

guess = input('Enter a guess: ')
guess = int(guess)   

if guess == number:
    print('You got it!')
elif guess < number:
    print('Too low!')
else:
    print('Too high!')    


# # Exercise: Calculator
# 
# 1. Ask the user to enter two different numbers, and assign them to the variables `first` and `second` again.
# 2. Ask the user a third question, to enter an operator (`+` or `-`).
# 3. If the user enters `+`, then show the two numbers and their sum.
# 4. If the user enters `-`, then show the two numbers and their difference.
# 5. If the user enters a different operator, give them an error message.
# 
# Example:
# 
#     Enter first: 10
#     Enter second: 5
#     Enter operator: +
#     10 + 5 = 15

# In[131]:


first = input('Enter first number: ')
second = input('Enter second number: ')

operator = input('Enter an operator: ')

first = int(first)
second = int(second)

if operator == '+':
    total = first+second
    print(f'{first} + {second} = {total}')

elif operator == '-':
    difference = first-second
    print(f'{first} - {second} = {difference}')
    
else:
    print(f'The operator {operator} is not supported.')


# In[132]:


x = 10
type(x)


# In[133]:


x = 10.0
type(x)


# In[134]:


x = 10.3
y = 5.7

x + y


# In[135]:


x - y


# In[136]:


0.1 + 0.2


# In[137]:


1/3


# In[138]:


# from str to int, we call "int" as a function
int('123')


# In[139]:


# from str to float, we call "float" as a function
float('123')


# In[140]:


# from int to float, use "float" as a function
float(123)


# In[141]:


# from float to int, use "int" as a function
int(123.456)   # it chops the number at the decimal point!


# In[142]:


# from int to str... use "str" as a function
str(123)


# In[143]:


# from float to str... use "str" as a function
str(123.456)


# In[144]:


1 + 2.3


# In[145]:


1 + 2.0


# # Data structure: Strings

# In[146]:


# We can create strings with '', "", or even f'' or f""

s = 'abcdefg'

# how long is s?  We can ask with the "len" function
len(s)


# In[147]:


# what if I want to print abc, then go down a line, and then print def?
s = 'abc
def'

print(s)


# In[148]:


# If we want to include a newline in the string, we type \n
# \n is translated into the character for a new line

s = 'abc\ndef'

print(s)


# In[149]:


# \n -- we type two characters, but in the string, it's seen as one
len(s)


# In[151]:


# To retrieve characters from a string, use [] and a numeric index starting with 0

s = 'abcdefghijklmnopqrstuvwxyz'


# In[152]:


s[0]  # return the first character in the string s


# In[153]:


s[1]


# In[154]:


s[2]


# In[155]:


# the final letter
s[25]


# In[156]:


i = 25
s[i]  # you can use a variable as an index


# In[157]:


# What if I don't know how long s is, and I want its final character
s[len(s)-1]


# In[158]:


s[99999]


# # Exercise: Retrieve from the string
# 
# 1. Ask the user to enter a string, and assign it to `s`.
# 2. Ask the user to enter a numeric index, and assign it to `i`.
# 3. If `i` is < 0 or too high, then print an error message.
# 4. Otherwise, print the index and character.
# 
# Example:
# 
#     Enter a string: hello
#     Enter an index: 100
#         100 is too high
#         
#     Enter a string: hello
#     Enter an index: 1
#         index 1 is e

# # Strategy:
# 
# 1. Ask the user to enter a string (`input`) and assign to `s`.
# 2. Ask the user to enter an integer `i`.  But of course, we get it as a string, so we'll need to convert it to an integer.
# 3. Check:
#     - is `i` < 0?  If so, then scold the user
#     - is `i >= len(s)`?  If so, then scold the user
#     - Print `i` and `s[i]`

# In[164]:


s = input('Enter string: ')
i = input('Enter numeric value: ')
i = int(i)

if i < 0:
    print(f'{i} is < 0!')
     
elif i >= len(s):
    print(f'{i} is >= than s')
    
else:
    print(f'character in the string {i} is {s[i]}')


# In[160]:


s


# In[161]:


s[len(s)-1]  # final character


# In[162]:


s[-1]   # final character


# In[163]:


s[-2]  # second to final character


# In[170]:


# Setup
s= input ('Enter a string: ')
i= input ('Enter a index: ')
i=int(i)

size = len(s)-1 
print(size)

# Calculations + report
if i > size:
    print (f' {i} to high, insert a value less than or equal {size}')
elif i < 0:  
    print(f'{i} too low!')
else:
    print (f' the caracter defined according index is :')
    print (s[i])
    


# # Tomorrow:
# 
# - Keep talking about strings
#     - Slices
#     - `in` and searching
# - Loops
#     - `for` loops on strings
#     - `for` loops on ranges
#     - `while` loops
# - Lists
#     - Mutable data vs. immutable data
#     - How are lists similar to strings (and how are they different)?
#     - Strings -> lists and back!
