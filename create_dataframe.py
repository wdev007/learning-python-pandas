import numpy as np
import pandas as pd

d = {'x': [1, 2, 3], 'y': np.array([2, 4, 8]), 'z': 100}

df_01 = pd.DataFrame(d)

print(df_01.count())

df_02 = pd.DataFrame(d, index=[100, 200, 300], columns=['z', 'y', 'x'])

print(df_02.count())

df_03 = pd.DataFrame([{'x': 1, 'y': 2, 'z': 100},
                      {'x': 2, 'y': 4, 'z': 100},
                      {'x': 3, 'y': 8, 'z': 100}])

print(df_03.count())

arr = np.array([[1, 2, 100],
                [2, 4, 100],
                [3, 8, 100]])

df_04 = pd.DataFrame(arr, columns=['x', 'y', 'z'])

print(df_04.count())

df_05 = pd.read_csv('data.csv', delimiter=',',index_col=0)

print(df_05.count())