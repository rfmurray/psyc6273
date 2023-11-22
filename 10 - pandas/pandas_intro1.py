# pandas_intro1.py

import numpy as np
import pandas as pd

# 1. creating a new DataFrame object

# we can create a data frame manually; we can specify column indices,
# row indices, and data
df = pd.DataFrame( {
        "Name": [ "Braund, Mr. Owen Harris", "Allen, Mr. William Henry", "Bonnell, Miss. Elizabeth" ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"] },
    index = ['a', 'b', 'c'])

# we can also read the data frame from a text file; here the row indices
# are integers
df = pd.read_csv("titanic.csv")  # also see pd.read_excel()

# some important properties of a DataFrame
df.describe()
df.info()
df.columns
df.index
df.dtypes


# 2. creating a new Series object

s = pd.Series(np.random.randn(5))
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
s = pd.Series({"b": 1, "a": 0, "c": 2}, name='rating')

# some important properties of a Series
s.values
s.name
s.index
s.dtype


# 3. selecting columns and rows from a DataFrame

# method 1: standard Python/NumPy expressions

# select columns
df['Age']           # returns a Series
df[['Age', 'Sex']]  # returns a DataFrame

# select rows
df[0:3]
df[df['Age']>35]

# select rows and columns
df[df['Age']>35]['Name']

# method 2: use indices with loc

df.loc[0:5]                   # rows
df.loc[:, 'Age']              # column
df.loc[:, ['Age', 'Sex']]     # columns
df.loc[0:5, ['Age', 'Sex']]   # rows and columns
df.loc[df['Age']>35, 'Name']  # rows and column

# method 3: use row and column numbers with iloc

df.iloc[0:10,3:6]  # can select rows, columns or both


# 4. indices are not just synonyms for row numbers

# (a) arithmetic operations on series and data frames follow indices,
# not row numbers

df1 = pd.DataFrame( {'a' : [10, 20, 30, 40], 'b': [100, 200, 300, 400]},
                    index = [ 'w', 'x', 'y', 'z' ])

df2 = pd.DataFrame( {'a' : [1, 2, 3, 4], 'b': [5, 6, 7, 8]},
                    index = [ 'x', 'y', 'z', 'w' ])

df3 = df1 + df2

# also, missing values are propagated through arithmetic operations

df4 = pd.DataFrame( {'a' : [1, 2, 3, 4], 'b': [5, 6, 7, 8]},
                    index = [ 'u', 'v', 'y', 'z' ])
df5 = df1 + df4

df6 = pd.DataFrame( {'a' : [1, 2, 3, 4], 'c': [5, 6, 7, 8]},
                    index = [ 'w', 'x', 'y', 'z' ])
df7 = df1 + df6

# (b) indices can be repeated

df8 = pd.DataFrame( {'a' : [1, 2, 3, 4], 'b': [5, 6, 7, 8]},
                    index = [ 'x', 'x', 'y', 'z' ])

df8.loc['x']
