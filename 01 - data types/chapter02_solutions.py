# chapter02_solutions.py

# 1. Practise Python arithmetic by calculating the following values at the
# console or in a script.

# (a)
3 ** 2

# (b)
((3*4) / (10+12-1))**5

# (c)
4 ** (2*3)

# (d)
(4*2) ** 3

# (e)

(4**2) * 3

# 2. Practise creating and using variables by doing the following.

# (a) Create a floating point variable length with a value of 3.4, that
# represents the length a of the side of a cube.
length = 3.4

# (b) Create a variable volume that equals the volume of the cube.
volume = length ** 3

# (c) Create a variable area that equals the area of the cube.
area = 6 * length ** 3

# We could use parentheses as well, to make the order of operations
# clearer to the reader.
area = 6 * (length ** 2)

# (d) Create a variable av_ratio that equals the ratio of area to volume of the cube.
av_ratio = area / volume

# Alternatively, we can observe that
#     area / volume = 6*(length**2) / (length**3) = 6 / length
# and calculate the ratio directly from the length.
av_ratio = 6 / length

# 3. Practise list operations by doing the following.

# (a) Create a list called x that contains the integers -5 to 5. You can
# just type in the numbers manually.
x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# (b) Create a variable a that equals the third element of x.
a = x[2]

# (c) Create a variable b that is a list that contains the third to seventh
# elements of x.
b = x[2:7]

# Notice that choosing the start and end points of a slice takes some
# attention to detail. To start the slice at the third element, we recall
# that numbering starts at zero, so the number we put before the colon is 2.
# To end the slice at the seventh element, again we recall that numbering
# starts at zero, but also that the second number in the slice notation
# is exclusive, so the number we put after the colon is 7.

# (d) Create a variable c that equals the absolute value of the fourth
# element of x.
c = abs(x[3])

# (e) Create a variable d that equals the first element of x to the power
# of the eighth element of x. Do this using the function pow().
d = pow(x[0], x[7])

# (f) Create a variable e that equals the first element of x to the power
# of the absolute value of the eighth element of x.
e = pow(x[0], abs(x[7]))

# (g) Make the fourth element of x equal to 100.
x[3] = 100

# 4. If the variable x is a tuple instead of a list, which parts of the
# previous question can still be solved, and which cannot be solved? Why?
# 
# answer: We can still solve parts (a) to (f). In fact, the solutions are
# more or less the same for a tuple as for a list. For example, the
# solution for part (b) is the same if x is a tuple.
a = x[1]

# For part (c), if we want the new variable b to be a tuple that contains
# the third to seventh elements of x, then the solution is the same.
b = x[2:7]

# Here, the new variable b is a tuple. (You can check this using type()).
# Strictly speaking, the problem  says that the variable b should be a
# list, so if we want to get that detail right then we can use the list()
# function to convert the tuple to a list.
b = list(x[2:7])

# We can't solve part (g) directly, since tuples are immutable.
# One workaround would be to convert the tuple to a list, change the
# fourth element, and convert the result back to a tuple.
x = list(x)
x[3] = 100
x = tuple(x)

# 5. Show that the return value of print('Hello, world!') is None.
x = print('Hello, world!')
print(x)

# Here the output is None.

# 6. Explore how Python sometimes automatically converts one data type
# to another.

# (a) Create variables a = 1 and b = 2, and show that their type is integer.
# Create another variable c = a / b,and show that its type is float.
a = 1
b = 2
type(a)
type(b)

# Here the output in both cases is <class 'int'>.

c = a / b
type(c)

# Here the output is <class 'float'>.

# (b) Create an integer variable with value 10, and a Boolean variable with
# value True. Add the two variables, and check the type and value of the
# result. What do you conclude about the value of True when it’s converted
# to an integer?
a = 10
b = True
c = a + b
type(c)
print(c)

# Here c has type 'int' and value 11. When the Boolean value True is
# treated as an integer, it has value one.

# (c) Repeat part (b), but this time add an integer to the Boolean value
# False. What value does False have when it’s converted to an integer?
a = 10
b = False
c = a + b
type(c)
print(c)

# Here c has type 'int' and value 10. When the Boolean value False is
# treated as an integer, it has value zero.

# (d) Repeat part (b), but this time add an integer to the value None.
# What happens?
a = 10
b = None
c = a + b

# In this case we get an error saying that an integer cannot be added
# to None. We might have thought that None would have a value of zero
# (like False), but that is not the case.

# 7. Here are some lines of code that may look unusual at first. Use what
# you’ve learned in this chapter to try to predict the result of each line,
# and justify your prediction. Run the code to see if your predictions are
# correct.

# (a) 'target dot'[:6]

# Here 'target dot' is a string, and we use slice notation to get elements
# zero through five, so the result is the string 'target'.

# (b) 'target dot'[7:][0]

# Here again, 'target dot' is a string, and now we use slice notation to
# get elements 7 to the end, which returns 'dot'. That return value is
# a string too, so it's perfectly fine to use indexing notation on it.
# Here we use indexing notation to get element 0, so the result is the
# first element of 'dot', which is the string 'd'.

# (c) 'target dot'.count('D')

# In this case we count the occurrences of the string 'D' in the string
# 'target dot'. The counting is case-sensitive, so the result is the
# integer 0.

# (d) 'target dot'.upper().replace('TARGET ', '').count('D')

# Here we first convert 'target dot' to uppercase, so the result is the
# string 'TARGET DOT'. With this string we replace the substring 'TARGET '
# with the empty string '', so the result is 'DOT'. Finally we count the
# occurrences of 'D' in 'DOT', so the result is the integer 1.

# (e) a = 20, 30, 40
#     a = a + a + a

# The first line assigns a the tuple (10, 20, 30), using the shortcut in
# which we don't use the parentheses. The second line re-assigns a
# to be the tuple (10, 20, 30) replicated three times, so the result is
# that a has the value (10, 20, 30, 10, 20, 30, 10, 20, 30).

# (f) x = [10, 20, 30]
#     x.append(40).append(50)

# The first line assigns x the list [10, 20, 30].
# 
# We might think that the second line appends the value 40 to x, and then
# appends the value 50, so that x becomes [10, 20, 30, 40, 50]. However,
# that is not correct.
# 
# In fact, the second line appends the value 40 to x, but it appends
# it in place, so the return value of x.append(40) is None. As a result,
# the rest of the line attempts to append the value of 50 to None, but
# None is not a list and doesn't have an append() method, so we get an
# error message.
# 
# To append 40 and then 50 to x, we should do the following instead.
x = [10, 20, 30]
x.append(40)
x.append(50)

# Or we could extend the list with both values at once.
x = [10, 20, 30]
x.extend([40, 50])

# (g) x = [10, 20, 30, 40, 50]
#     x.extend(x[:2])

# The first line assigns a list to x. The second line extends x with a
# list that is x[:2], which is [10, 20], so the result is that x has the
# value [10, 20, 30, 40, 50, 10, 20].

