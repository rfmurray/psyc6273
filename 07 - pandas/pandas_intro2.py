# pandas_intro2.py

import pandas as pd

# load some data
df = pd.read_csv('titanic.csv')  # also see pd.read_excel()

# sort by data columns
df.sort_values(by='Pclass', inplace=True)
df.sort_values(by=['Pclass', 'Fare'], ascending=False, inplace=True)

# summary statistics (aggregation)
df['Age'].mean()           # number
df[['Age','Fare']].mean()  # series
df[['Age','Fare']].std()   # series
df[['Age','Fare']].agg(['mean', 'std', 'sum', 'count'])  # data frame

# summary statistics on groups
df.groupby('Pclass')['Age'].mean()  # series

# detour to show groups
df.groupby('Pclass').apply(print)

# back to summary statistics on groups
df.groupby('Pclass')['Age'].mean()           # series
df.groupby('Pclass')[['Age','Fare']].mean()  # data frame
df.groupby(['Pclass', 'Sex'])[['Age','Fare']].mean()  # data frame with a multi-index

# detour on multi-indices
df2 = df.groupby(['Pclass', 'Sex'])[['Age','Fare']].mean()
df2.loc[(1,'female'),'Age']  # can use a tuple as a multi-index
df2.loc[(3,'female'),'Fare']

# back to summary statistics on groups
df.groupby(['Pclass', 'Sex'])[['Age','Fare']].mean()  # data frame with a multi-index
df.groupby(['Pclass', 'Sex'])[['Age','Fare']].std()
df.groupby(['Pclass', 'Sex'])[['Age','Fare']].count()
df.groupby(['Pclass', 'Sex'])[['Age','Fare']].agg(['mean', 'std', 'count'])  # data frame with two multi-indices

# another use of multi-indices
df3 = df.groupby(['Pclass', 'Sex'])[['Age','Fare']].agg(['mean', 'std', 'count'])
df3.loc[(2,'female'),('Age','mean')]
