import numpy as np
import pandas as pd

df = pd.read_csv('data.csv', delimiter=',', index_col=0)

print(df['name'])

print(df.loc[101])

print(df.loc[101:103, ['name', 'city']])

df.loc[101:103, 'score'] = [1, 2, 3]

print(df)