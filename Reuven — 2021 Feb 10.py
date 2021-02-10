#!/usr/bin/env python
# coding: utf-8

# In[1]:


from friendly_traceback.ipython import *


# # Agenda
# 
# 1. Talk about `str.split` and `str.join`
# 2. Dictionaries
# 3. Files
# 4. PyCharm

# If I have data d of type X and I want data of type Y, I can just say
# 
# `Y(d)`   # give me a new piece of Y data, based on d

# In[2]:


int('12345')  # we're getting an int based on a string


# In[3]:


str(2468) # getting a string based on an int


# In[4]:


# to move from string to list, we can use "list"
list('abcde')


# In[5]:


# to move from list to string, we can use "str"
mylist = [10, 20, 30]
str(mylist)


# In[7]:


# but sometimes, we want to move from list->string and string->list differently

record = 'firstname|lastname|age'

# how can I turn this into a list, with each element being a different field of the record?

# I can use the "str.split" method (the split method for strings)

record.split('|')  # return a list of strings, whose elements are from record, separated by |


# In[8]:


words = 'This is a bunch of words'
words.split(' ')


# In[9]:


words = 'This   is a bunch  of    words'
words.split(' ')


# In[10]:


words = 'This   is a bunch  of    words'
words.split()  # no argument at all -- meaning, all whitespace, any length


# In[11]:


words


# In[12]:


# str.split takes a string, and returns a list of strings
# str.join takes a list of strings, and returns one string

words = words.split()  # now, "words" is a list of strings
words


# In[13]:


# I can use str.join to get a new string back!
# the string used in str.join is the "glue" put between elements of the list

# glue.join(list_of_strings)
'*'.join(words)


# In[14]:


words


# In[15]:


' '.join(words)


# In[18]:


words = ' This    is the bunch of wwordssssss'
'*'.join(words)  # argument is an iterable of strings -- a string!


# In[19]:


'*'.join(words.split())  # argument is a list of strings


# In[ ]:





# # Exercise: Pig Latin a sentence
# 
# 1. Ask the user to enter a sentence in English (no capitals, no punctuation)
# 2. Translate the sentence into Pig Latin, printing the translation on a single line
# 
# For now: 
# 1. Ask the user to enter a sentence
# 2. Turn the sentence into a list of strings, using `str.split`
# 3. Go through the words in the sentence, one at a time, and print them *translated into Pig Latin*

# In[22]:


sentence = input('Enter a sentence: ')

words = sentence.split()   # no argument means: any whitespace is a separator

for word in words:
    print(word)


# In[23]:


word = input('Enter a word: ')

if word[0] in 'aeiou':
    print(word + 'way')
else:
    print(word[1:] + word[0] + 'ay')


# In[24]:


sentence = input('Enter a sentence: ')

words = sentence.split()   # no argument means: any whitespace is a separator

for word in words:
    if word[0] in 'aeiou':
        print(word + 'way')
    else:
        print(word[1:] + word[0] + 'ay')


# # Exercise: Pig Latin sentence, part 3
# 
# 1. Create an empty list, and assign it to `output`.
# 2. In our `for` loop, when we're translating words into Pig Latin, we're *not* going to print them on the screen.  Rather, we'll use `list.append` to add the translation to the end of the `output` list.
# 

# In[25]:


mylist = [10, 20, 30]
mylist.append(40)   # append adds the item to the end of the list
mylist.append(50)  


# In[26]:


mylist


# In[27]:


mylist = []
mylist.append(10)
mylist.append(20)

mylist


# In[29]:


output = []

sentence = input('Enter a sentence: ')

words = sentence.split()   # no argument means: any whitespace is a separator

for word in words:
    if word[0] in 'aeiou':
        output.append(word + 'way') 
    else:
        output.append(word[1:] + word[0] + 'ay')  
        
output


# # Exercise: Pig Latin sentence, part 4
# 
# Instead of just displaying/returning `output`, turn it into a string, and print that out.
# 
# Remember: The `str.join` method:
# - Runs on a string, the "glue"
# - The argument (in parentheses) is a list of strings/words to join together
# - The method returns a string

# In[31]:


mylist = ['abcd', 'efgh', 'ijklm']

s = '*'.join(mylist)  # '*' is what we're running the method on, the "glue"
                  # mylist is the variable containing a list of strings
    
# Notice: When we do this, mylist DOES NOT CHANGE!
# str.join returns a new string, which we can use in assignment or printing

print(s)


# In[33]:


output = []

sentence = input('Enter a sentence: ')

words = sentence.split()   # no argument means: any whitespace is a separator

for word in words:
    if word[0] in 'aeiou':
        output.append(word + 'way') 
    else:
        output.append(word[1:] + word[0] + 'ay')  
        
s = ' '.join(output)
print(s)


# In[34]:


s


# In[35]:


# numbers, separated by | characters
s = '10|20|30|40|50|60'

# I want this string as it is, *BUT* each number should
# be translated into binary (just 1s and 0s)


# In[36]:


bin(25)


# In[39]:


# If I want to translate this string:
# (1) Create an output list
# (2) Break up s into individual fields
# (3) Turn each element into an integer
# (4) Run "bin" on each element
# (5) Add each translated element to our output list
# (6) Join that together with | characters

s = '10|20|30|40|50|60'
output = []

fields = s.split('|')  # get a list of strings back

for one_field in fields:
    binary_field = bin(int(one_field))
    output.append(binary_field)
    
output_string = '|'.join(output)
print(output_string)


# In[42]:


mylist = [['ab', 'cd', 'ef'],
          ['gh', 'ij', 'kl'],
          ['mno', 'pqrst', 'uvw']]

output = []
for one_record in mylist:
    one_string_record = ','.join(one_record)
    output.append(one_string_record)

output_text = '\n'.join(output)    
print(output_text)


# # Data structure: Dictionaries
# 
# Dictionaries have many different names:
# - Hash tables
# - Hashes
# - Hash maps
# - Maps
# - Associative arrays
# - Key-value stores
# - Name-value stores

# In[43]:


# To create a new dictionary, we use {} 
# inside, we have key-value pairs
# each key-value pair is separated by a colon
# the pairs are separated from one another with commas

d = {'a':1, 'b':2, 'c':3}     # key:value, key:value, key:value

# here, my pairs are:
# 'a' - 1
# 'b' - 2
# 'c' - 3

# Unlke a list or string, the keys/indexes are strings!
# in a dict, the keys can be anything immutable (basically, numbers and strings)
# the values can be anything at all


# In[44]:


d['a']   # meaning: give me the value in dict d for key 'a'


# In[45]:


d['b']  # give me the value in dict d for key 'b'


# In[46]:


person = ['Reuven', 'Lerner', 46]
person[0]  # first name


# In[47]:


person[1] # last name


# In[48]:


person[2]  # shoe size


# In[49]:


person = {'first':'Reuven', 'last':'Lerner', 'shoesize':46}


# In[50]:


person['first']


# In[51]:


person['last']


# In[52]:


person['shoesize']


# In[53]:


person['height']


# In[54]:


explain()


# In[55]:


# The "in" operator works on dictionaries, too!
# it checks if something is a *key*  (never a value)

'shoesize' in person   # meaning: is 'shoesize' a key in the "person" dict?


# In[56]:


'height' in person   # meaning: is 'height' a key in the "person" dict?


# # Dictionary basics
# 
# 1. Dicts contain key-value pairs
#     - Keys can be numbers or strings
#     - Values can be *anything* at all
# 2. We define dicts with `{}`
#     - `d = {'a':1, 'b':2, 'c':3}`
# 3. We use `[]` to retrieve a value based on a key
#     - `d['a']`  # returns 1
#     - `d['b']`  # returns 2
# 4. If you request a key that doesn't exist, you get a `KeyError`
# 5. You can use `in` to check if a key is in a dict
#     - `'a' in d`  # returns True
#     - `'x' in d`  # returns False
#     - `1 in d` # returns False -- we only check the keys!

# # Exercise: Restaurant menu
# 
# 1. Define a dictionary, called `menu`, in which the keys are the items on a restaurant menu and the values are the prices.
# 
# 2. Ask the user to order one item from the menu.
# 3. If the item is on the menu, print the price.
# 4. If the item is *not* on the menu, then scold the user.
# 
# Example:
# 
#     Order: sandwich
#     sandwich costs 10
#     
#     Order: elephant
#     We are fresh out of elephant today

# In[57]:


d


# In[58]:


s = input('Enter a key: ')

d[s]  # since s is 'a', d[s] is the same as d['a']


# In[59]:


# create the dict with {}
menu = {'sandwich':10, 'tea':5, 'cake':7, 'apple':2}

type(menu)


# In[60]:


# retrieve from the dict with []
menu['sandwich']


# In[61]:


order = 'sandwich'
menu[order]


# In[67]:


menu = {'sandwich':10, 'tea':5, 'cake':7, 'apple':2}

order = input('Order: ')

if order in menu:  # is the user's input *really* a key in our dict?
    price = menu[order]
    print(f'The price of {order} is {price}.')
else:
    print(f'We are out of {order} today.')


# # Exercise: Restaurant menu, part 2
# 
# 1. Define a variable, `total`, to be 0.
# 2. Modify the existing code, so that we ask the user repeatedly what they want ot order.
#     - This means: Use a `while` loop!
# 3. If the user enters an empty string, then `break` from the loop.
# 4. If the user enters something on the menu, then assign `price` the price of the item (from the dict), update `total`, and print the price and new total.
# 5. If the user enters something not on the menu, then say we're out of it today.
# 6. At the end, print the total.
# 
# Remember:
# - We can ask repeatedly with `while True`, so long as we also have a way to `break` from the loop
# 
# Example:
# 
#     Order: sandwich
#     sandwich is 10, total is 10
#     Order: tea
#     tea is 5, total is 15
#     Order: elephant
#     We're out of elephant today
#     Order: [ENTER]
#     Your total is 15

# In[2]:


# (1) create the total variable, set to 0
total = 0

menu = {'sandwich':10, 'tea':5, 'cake':7, 'apple':2}

while True:  # (2) infinite loop asking for an order

    order = input('Order: ')

    # (3) is the order an empty string? If so, then exit the loop
    if order == '':
        break

    if order in menu: 
        price = menu[order]
        # (4) add the price to the total
        total += price
        print(f'The price of {order} is {price}, total is {total}.')
    else:
        print(f'We are out of {order} today.')
        
# (5) print the total        
print(f'total = {total}')


# In[3]:


d = {'a':1, 'b':2, 'c':3}

# to add a new key-value pair to my dict, just assign
d['x'] = 100

d


# In[4]:


# to update an existing value, just assign
d['x'] = 2345

d


# In[5]:


all_prices = []

menu = {'sandwich':10, 'tea':5, 'cake':7, 'apple':2}

while True: 

    order = input('Order: ')

    if order == '':
        break

    if order in menu: 
        price = menu[order]
        all_prices.append(price)
        print(f'The price of {order} is {price}, total is {sum(all_prices)}.')
    else:
        print(f'We are out of {order} today.')

print(f'all_prices = {all_prices}')
print(f'total = {sum(all_prices)}')


# In[ ]:





# In[6]:


# count how many times each vowel is in a sentence 

counts = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

s = input('Enter a string: ')

for one_character in s:
    if one_character in 'aeiou':
        counts[one_character] += 1

print(counts)


# # Exercise: vowels, digits, and others (dict edition)
# 
# 1. Create a dict with keys `vowels`, `digits`, and `others`, and all values will be 0.
# 2. Ask the user to enter *ONE* string.
# 3. Use a `for` loop to iterate over every character in the string.
#     - If the character is a vowel, update the count of vowels
#     - If the character is a digit, update the count of digits
#     - Otherwise, update the count of "others"
# 4. Print the dict
# 
# Hints:
# - We can iterate over a string, one character at a time, with a `for` loop
# - We can check if something is a vowel with `in`: `if x in 'aeiou'`
# - We can check if a string contains only digits with `str.isdigit`
# - We can add to the count of something with `+=`
#  

# In[10]:


d = {'vowels':0, 'digits':0, 'others':0}

s = input('Enter a string: ')

for one_character in s:
    if one_character in 'aeiou':
        d['vowels'] += 1
    elif one_character.isdigit():
        d['digits'] += 1
    else:
        d['others'] += 1
    
print(d)


# In[11]:


x = 100


# In[12]:


print(d)


# In[13]:


# we can iterate over a dictionary!

for one_item in d:
    print(one_item)


# In[14]:


for one_key in d:
    print(f'{one_key}: {d[one_key]}')


# In[15]:


'vowels' in d


# In[16]:


'digits' in d


# In[17]:


mylist = [10, 20, 30, 40, 50]

30 in mylist


# In[18]:


d = {'a':1, 'b':2, 'c':3}

'a' in d


# In[19]:


d = {'a':1, 'b':2, 'c':3, 'a':10, 'b':20, 'c':30}


# In[20]:


d


# In[21]:


counts = {}  # empty dict!

s = input('Enter a string: ')

for one_character in s:

    # first time seeing this character? Give it a count of 0
    if one_character not in counts:
        counts[one_character] = 0
        
    counts[one_character] += 1
    
print(counts)


# # Files
# 
# To work with files, we'll need a helper -- known in many languages as a "file handle," but in Python it's known as a "file object" or even a "file-like object."
# 
# We'll get a file object when we "open" a file.  Then we can either read from our file (via the file object) or write to the file (via the file object).
# 
# When we're done working with the file, we "close" it.
# 
# Typically, we only read from or write to a file -- not both.

# In[23]:


# If I want to read from a file:

# (1) open it
# (2) run the "read" method on it, returning a string
# (3) close it

f = open('/etc/passwd')   # this opens the file, and puts a file object in f
print(f.read())           # the "read" method returns a string -- the contents of the file
f.close()                 # I don't want to work with the file any more


# In[25]:


# (1) open the file for reading (the default), get f, the file object
# (2) Iterate over the file object in a "for" loop
# (3) get each line of the file, one at a time

f = open('/etc/passwd')   # this opens the file, and puts a file object in f
for one_line in f:
    print(one_line.strip())  # strip removes whitespace on the edges, not inside
f.close()                 # I don't want to work with the file any more


# # Exercise: Print a file
# 
# 1. Open the file `/etc/passwd`, and assign to `f`
# 2. Iterate (in a `for` loop) over `f`, one line at a time
# 3. Print each line.  If you care about the whitespace, use `strip` on the string variable to remove whitespace.

# In[26]:


open('/etc/passwd')


# In[27]:


f = open('/etc/passwd')

for one_line in f:
    print(one_line)


# In[28]:


print(open('/etc/passwd').read())


# # Exercise: Searching in the file
# 
# 1. Ask the user to enter a string, call it `look_for`.
# 2. Iterate over `/etc/passwd`, one line at a time.
# 3. If a line contains `look_for`, then print that line.
# 

# In[32]:


# only print lines containing 'a'

# (1) ask the user to enter a search string

for one_line in open('/etc/passwd'):
    if 'z' in one_line:   # (2) modify this line to look for the search string, not 'z'
        print(one_line)


# In[36]:


look_for = input('Enter search string: ')

for one_line in open('/etc/passwd'):
    if look_for in one_line:
        print(one_line.strip())


# In[38]:


# Print all of the usernames from the file
# Hint: the usernames are the first field (index 0) in each line

for one_line in open('/etc/passwd'):
    print(one_line.split(':')[0])


# In[39]:


get_ipython().system('ls *.txt')


# In[40]:


get_ipython().system('head mini-access-log.txt')


# # Exercise: Print IP addresses
# 
# 1. Open and iterate over `mini-access-log.txt` (in the current directory).
# 2. Grab the IP address from each line, and print it out.

# In[41]:


get_ipython().run_line_magic('pwd', '')


# In[49]:


for one_line in open('mini-access-log.txt'):
    print(one_line.split()[0])


# In[50]:


counts = {}  # new dict

s = 'abcabcd'  # count how many times each letter appears, using a dict

for one_character in s:
    
    # is one_character already in counts?  If not, then add it with a value of 0
    if one_character not in counts:
        counts[one_character] = 0
        
    # we know that one_charcter is a key in the dict
    # so we can just add 1 to it
    counts[one_character] += 1
    
counts


# # Exercise: Counting IP addresses in a file
# 
# Using the code that we've already written:
# 
# ```python
# for one_line in open('mini-access-log.txt'):
#     print(one_line.split()[0])
# ```
# 
# 1. Create a new, empty dict called `counts`
# 2. As you iterate over the lines of `mini-access-log.txt`, grab the IP address (don't print it) and assign it to a variable (`ip_address`)
# 3. Is this the first time we're seeing the IP address?  If so, then add it as a key to the `counts` dict, with a value of 0
# 4. No matter what, add 1 to the count for this IP address
# 5. print `counts`

# In[51]:


counts = {}  # new dict

for one_line in open('mini-access-log.txt'):
    
    # (1) get the IP address 
    ip_address = one_line.split()[0]

    # (2) is the IP address already a key in counts?
    if ip_address not in counts:
        counts[ip_address] = 0
        
    # (3) no matter what, increment the count for this IP address
    counts[ip_address] += 1
    
counts

      6     if ip_address not in counts:
      7         counts[ip_address] = 0
----> 8     counts[ip_address] += 1

# In[52]:


counts


# In[54]:


for ip_address in counts:
    print(f'{ip_address}:\t{counts[ip_address]}')


# In[55]:


3 * 5


# In[56]:


3 * 'x'


# In[58]:


for ip_address in counts:
    print(f'{ip_address}:\t\t{counts[ip_address] * "x"}')


# In[59]:


get_ipython().system('ls *.txt')


# In[60]:


get_ipython().system('head shoe-data.txt')


# In[ ]:


f = open('/etc/passwd', 'r')    # opening for reading, explicitly 
f.read()


# In[61]:


# opening a file means ERASING ANYTHING THAT WAS PREVIOUSLY THERE!

f = open('rml-output.txt', 'w') # opening for writing (using 'w')
f.write('abcd\n')   # unlike print, you *MUST* add a newline explicitly with .write
f.write('efghij\n')
f.close()           # if you don't close a file, it might not get written for a while


# In[62]:


get_ipython().system('cat rml-output.txt')


# # Exercise: Writing to files
# 
# 1. Open a file for writing.  Choose a filename with your name/initials/something unique.
# 2. Run a `for` loop 5 times.   (That means using `range(5)`.)
# 3. In each iteration, ask the user to enter a string.
# 4. Write the string to the file, on a line by itself.  (Don't forget to use `\n` at the end.)
# 5. Close the file.
# 

# In[68]:


f = open('rml-output.txt', 'w') 

for i in range(5):
    s = input(f'{i} Enter a string: ')
    f.write(f'{s}\n')

f.close()      


# In[64]:


get_ipython().system('cat rml-output.txt')


# In[65]:


for one_line in open('rml-output.txt'):
    print(f'{one_line.strip()}, {len(one_line.strip())}')


# In[66]:


for i in range(5):  # iterate 5 times, from 0 through 4
    print(i)


# In[ ]:




