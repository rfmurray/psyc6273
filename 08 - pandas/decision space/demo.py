
import pandas as pd

df1 = pd.read_csv('demo.txt',delimiter=',', header=None)
df1.columns = ['c1', 'c2', 'v']
print(df1)
print()

df2 = pd.pivot_table(df1, index='c1', columns='c2', values='v')
print(df2)
