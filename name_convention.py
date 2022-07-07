

Naming Conventions

'''
Always use meaningful and intention-revealing names. 
It's always better to use long, descriptive names than short names with comments.

1. Use nouns for variable names
2. Use descriptive/intention-revealing names

'''

# This is bad
# represents the number of active users
au = 55

# This is good
active_user_amount = 55


'''
Variables

Other developers should be able to figure out what a variable stores just by reading its name.
'''

# This is bad
c = 5
d = 12

# This is good
city_counter = 5
elapsed_time_in_days = 12


'''
3. Use pronounceable names

You should always use pronounceable names; otherwise, you'll have a hard time explaining your algorithms out loud.
'''


from datetime import datetime

# This is bad
genyyyymmddhhmmss = datetime.strptime('04/27/95 07:14:22', '%m/%d/%y %H:%M:%S')

# This is good
generation_datetime = datetime.strptime('04/27/95 07:14:22', '%m/%d/%y %H:%M:%S')

'''
4. Avoid using ambiguous abbreviations (D)

Don't try to come up with your own abbreviations. It's better for a variable to have a longer name than a confusing name.
'''


# This is bad
fna = 'Bob'
cre_tmstp = 1621535852

# This is good
first_name = 'Bob'
creation_timestamp = 1621535852

'''
5. Always use the same vocabulary

Avoid using synonyms when naming variables.
'''

# This is bad
client_first_name = 'Bob'
customer_last_name = 'Smith'

# This is good
client_first_name = 'Bob'
client_last_name = 'Smith'


'''
6. Don't use "magic numbers"

Magic numbers are strange numbers that appear in code, which do not have a clear meaning. Let's take a look at an example:
'''

import random

# This is bad
def roll():
    return random.randint(0, 36)  # what is 36 supposed to represent?

# This is good
ROULETTE_POCKET_COUNT = 36

def roll():
    return random.randint(0, ROULETTE_POCKET_COUNT)
'''
Instead of using magic numbers, we can extract them into a meaningful variable.
'''



'''
7. Use solution domain names

If you use a lot of different data types in your algorithm or class and you can't figure them out from the variable name itself, 
don't be afraid to add data type suffix to your variable name.
For example:
'''


# This is good
score_list = [12, 33, 14, 24]
word_dict = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cherry',
}

# And here's a bad example (because you can't figure out the data type from the variable name):

# This is bad
names = ["Nick", "Mike", "John"]

'''
8. Don't add redundant context

Do not add unnecessary data to variable names, especially if you're working with classes.
'''

# This is bad
class Person:
    def __init__(self, person_first_name, person_last_name, person_age):
        self.person_first_name = person_first_name
        self.person_last_name = person_last_name
        self.person_age = person_age


# This is good
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

'''
We're already inside the Person class, so there's no need to add a person_ prefix to every class variable.
'''





'''
Functions
1. Use verbs for function names
2. Do not use different words for the same concept

Pick a word for each concept and stick to it. Using different words for the same concept will cause confusion.
'''

# This is bad
def get_name(): pass
def fetch_age(): pass

# This is good
def get_name(): pass
def get_age(): pass

'''
3. Write short and simple functions
4. Functions should only perform a single task

If your function contains the keyword 'and' you can probably split it into two functions. Let's look at an example:
'''

# This is bad
def fetch_and_display_personnel():
    data = # ...

    for person in data:
        print(person)


# This is good
def fetch_personnel():
    return # ...

def display_personnel(data):
    for person in data:
        print(person)


'''
5. Keep your arguments at a minimum

The arguments in your function should be kept to a minimum. Ideally, your functions should only have one to two arguments. If you need to provide more arguments to the function, you can create a config object which you pass to the function or split it into multiple functions.

Example:
'''

# This is bad
def render_blog_post(title, author, created_timestamp, updated_timestamp, content):
    # ...

render_blog_post("Clean code", "Nik Tomazic", 1622148362, 1622148362, "...")


# This is good
class BlogPost:
    def __init__(self, title, author, created_timestamp, updated_timestamp, content):
        self.title = title
        self.author = author
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp
        self.content = content

blog_post1 = BlogPost("Clean code", "Nik Tomazic", 1622148362, 1622148362, "...")

def render_blog_post(blog_post):
    # ...

render_blog_post(blog_post1)


'''
6. Don't use flags in functions

Flags are variables (usually booleans) passed to functions, which the function uses to determine its behavior. 
They are considered bad design because functions should only perform one task. 
The easiest way to avoid flags is to split your function into smaller functions.
'''

text = "This is a cool blog post."


# This is bad
def transform(text, uppercase):
    if uppercase:
        return text.upper()
    else:
        return text.lower()

uppercase_text = transform(text, True)
lowercase_text = transform(text, False)


# This is good
def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()

uppercase_text = uppercase(text)
lowercase_text = lowercase(text)


'''
7. Avoid side effects

A function produces a side effect if it does anything other than take a value in and return another value or values. 
For example, a side effect could be writing to a file or modifying a global variable.

'''



'''
1. Don't comment bad code, rewrite it

Commenting bad code -- i.e., # TODO: RE-WRITE THIS TO BE BETTER -- only helps you in the short term.
'''


'''
2. Readable code doesn't need comments

If your code is readable enough you don't need comments. 
Adding useless comments will only make your code less readable. Here's a bad example:

'''

# This checks if the user with the given ID doesn't exist.
if not User.objects.filter(id=user_id).exists():
    return Response({
        'detail': 'The user with this ID does not exist.',
    })

'''
As a general rule, if you need to add comments, they should explain "WHY" you did something rather than "WHAT" is happening.
'''

'''
 Don't add noise comments
'''
#This is bad:

numbers = [1, 2, 3, 4, 5]

# This variable stores the average of list of numbers.
average = sum(numbers) / len(numbers)
print(average)


'''
3. Don't leave commented out code
'''






#TRICKS

#Decorators

def ask_for_passcode(func):
    def inner():
        print('What is the passcode?')
        passcode = input()

        if passcode != '1234':
            print('Wrong passcode.')
        else:
            print('Access granted.')
            func()

    return inner


@ask_for_passcode
def start():
    print("Server has been started.")


@ask_for_passcode
def end():
    print("Server has been stopped.")


start()  # decorator will ask for password
end()  # decorator will ask for password


#Context Managers

with open('wisdom.txt', 'w') as opened_file:
    opened_file.write('Python is cool.')

# opened_file has been closed.

#Without a context manager our code would look like this:

file = open('wisdom.txt', 'w')
try:
    file.write('Python is cool.')
finally:
    file.close()

#Iterators


names = ["Mike", "John", "Steve"]
names_iterator = iter(names)

for i in range(len(names)):
    print(next(names_iterator))

#Or use an enhanced loop:

names = ["Mike", "John", "Steve"]

for name in names:
    print(name)

