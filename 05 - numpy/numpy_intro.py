# numpy_intro.py  Introduction to the numpy module

# np is the standard short form for the numpy module
import numpy as np

# - the main class in numpy is the multidimensional array (ndarray)
# - elements are all of the same type; usually numbers
# - elements are indexed by non-negative integers, just like in lists and tuples
# - the dimensions of the array are also called 'axes'

# create an array of zeros
x = np.zeros(shape=(3,4))
x
type(x)

# some important attributes of an array
x.ndim      # number of dimensions
x.shape     # size of each dimension
x.size      # total number of elements
x.dtype     # data type of elements

# more ways of creating arrays

x = np.zeros(shape=(3,4))
x = np.ones(shape=(3,4))
x = np.empty(shape=(3,4))  # contents depend on what was previously in memory
x = np.full(shape=(3,4), fill_value=10)

x = np.random.normal(loc=0.0, scale=1.0, size=(3,4))
x = np.random.uniform(low=0.0, high=1.0, size=(3,4))

# - transform a sequence into a 1D array
x = np.array([ 1.0, 2.0, 3.0 ])  # transform a list
x = np.array(( 1.0, 2.0, 3.0 ))  # transform a tuple

# - transform a sequence of sequences into a 2D array
x = np.array([ [ 1.0, 2.0, 3.0 ], [ 4.0, 5.0, 6.0 ] ])  # list of lists
x = np.array([ ( 1.0, 2.0, 3.0 ), ( 4.0, 5.0, 6.0 ) ])  # list of tuples

# - can optionally specify a data type
x = np.array([1, 2, 3], dtype=np.float64) # a few types: uint8, int64, float32, float64 
x.dtype
x = np.array([1, 2, 3], dtype=np.uint8)
x.dtype

# - create 1D sequences of numbers
x = np.arange(10)  # data type is np.int64
x = np.arange(start=0.0, stop=100.0, step=20.0)  # step is step size
x = np.linspace(start=0.0, stop=100.0, num=6)    # num is number of steps
# with floating point numbers, it can be difficult to predict the number
# of elements returned by arange (e.g., rounding errors); better to use
# linspace

# - load data from a text file
x = np.loadtxt(fname='data.txt', comments='#', delimiter=',')

# arithmetic operations apply to whole arrays

x = np.random.normal(size=(3,4))
y = np.random.normal(size=(3,4))

z = x + y
z = x - y
z = x * y
z = x / y

x += 1
x -= 2
x *= 10
x /= 20

# functions that apply to whole arrays

u = np.exp(x)
v = np.log(u)
# others: all, any, argmax, argmin, ceil, clip, corrcoef, cov, cross, cumprod,
# cumsum, diff,  dot, floor, inner, max, mean, median, min, prod, round, sort,
# std, sum, trace, transpose, var

# indexing and slicing

x = np.random.normal(size=(10,5))

y = x[2,3]      # pick a single element: row, column; result is a number, not an array
type(y)         # np.float64, not np.ndarray
y.ndim          # zero-dimensional

y = x[0:5,1]    # multiple rows; result is a 1D array
y = x[:,1]      # all rows; result is a 1D array
y = x[1:3,:]    # multiple rows, all columns; result is a 2D array

x[:,1] = 0      # can also assign new values to parts of an array

