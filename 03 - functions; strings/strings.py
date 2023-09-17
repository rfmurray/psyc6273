# strings.py  Strings

# we can define a string using single quotes, double quotes, or triple quotes.

s = 'a simple example'  # single quotes

s = 'if we use single quotes, we can embed a "quoted passage" in the string'

s = "another simple example"  # double quotes

s = "when using double quotes, a string's content can include possessives"

s = """when using triple quotes,
the content of a string
can extend over several lines"""

s = '''a triple-quoted string can be created
using single (') or double (") quotes'''

# the newline is sometimes shown as \n instead of actually starting
# a new line

s
print(s)


# strings are sequences, so we can use all sequence operations on them

s = 'a test string for illustration'

s[0]
s[3:5]
s[::2]


# strings have many methods available. strings are immutable, so methods
# always return a value, instead of changing the string in place.

s = 'a test string for illustration'

i = s.find('for')  # find the index where a substring begins

i = s.find('xyz')

s = 'jfk,lbj,rmn,grf,jec'
x = s.split(',')   # split a string at a separator

t = s.replace(',',':')  # replace all occurrences of a substring


# there are several ways of embedding the values of variables in strings.
# the newest, best, and easiest is probably f-strings, which have been available
# from python 3.6 onwards.

height = 8.41315934
volume = 30.4193

s = f'the height is {height} cm and the volume is {volume} cm^3'

# we can also specify the format of the variable in the string.

s = f'the height is {height:.2f} cm and the volume is {volume:.2f} cm^3'

# the embedded format codes work like this:
# 
#     {[variable name]:[width].[decimals][data type]}
# 
# width = how many spaces the value should take up (at a minimum)
# decimals = number of decimal places (not allowed for int and string; see next line)
# data type = f for float, d for int, s for string

# for example, we can make a string containing floating point numbers with
# two decimal places, and make sure that each number takes up at least ten
# characters, so that they line up as columns in a table with many such strings.

s = f'{height:10.2f},{volume:10.2f}'

