# chapter05_solutions.py

# 1. In this chapter, we created f-strings using single quotes. Can you also
# create f-strings using double or triple quotes? Try and see if it works.

# Yes, we can create f-strings using double or triple quotes as well
# as single quotes.

x = 3.14
y = 2.718

test1 = f"results: {x}, {y}"
print(test1)

test2 = f'''results:
{x}
{y}'''
print(test2)

# 2. Recall that we can `unpack' the elements of a tuple like this:
# x, y = 10, 20. This looks quite similar to how we used two loop variables
# in a for loop with zip(). Write a script that uses type() to show that in
# a for loop, zip() actually returns a tuple. When we use two loop
# variables, we are simply unpacking this tuple.

x = [1, 2, 3]
y = ['a', 'b', 'c']
for u in zip(x, y):
    print(u, type(u))

# 3. In the Windows operating system, filename paths often use backslashes
# as separators, like this:
#     \User\rfm\Dropbox\experiment\data.txt
# Other operating systems, such as Linux and macOS, use forward slashes (/).
# Write a script that defines a variable filename1 that contains a filename
# with backslashes, and then use string operations to create filename2,
# which has backslashes replaced by forward slashes.

winfile = '\\User\\rfm\\Dropbox\\experiment\\data.txt'

# method 1
macfile = winfile.replace('\\', '/')

# method 2
macfile = '/'.join(winfile.split('\\'))

