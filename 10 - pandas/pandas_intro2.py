# pandas_intro2.py

import pandas as pd

# load some data
df = pd.read_csv('titanic.csv')  # also see pd.read_excel()

# sort by data columns
df.sort_values(by='Age', inplace=True)
df.sort_values(by=['Pclass', 'Age'], ascending=False, inplace=True)

# summary statistics (aggregation)
df[['Age','Fare']].mean()
df[['Age','Fare']].std()
df[['Age','Fare']].agg(['mean', 'std', 'sum', 'count'])

# summary statistics on groups
df.groupby('Pclass')['Age'].mean()
df.groupby('Pclass')[['Age','Fare']].mean()
df.groupby(['Pclass', 'Sex'])[['Age','Fare']].mean()
df.groupby(['Pclass', 'Sex'])[['Age','Fare']].std()
df.groupby(['Pclass', 'Sex'])[['Age','Fare']].count()
df.groupby(['Pclass', 'Sex'])[['Age','Fare']].agg(['mean', 'std', 'count'])

# can see information on the groups
df.groupby(['Pclass', 'Sex']).describe()
df.groupby(['Pclass', 'Sex']).apply(print)
