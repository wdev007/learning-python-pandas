import numpy as np
import pandas as pd

df = pd.read_csv('data.csv', index_col=0)

john = pd.Series(data=['John', 'Boston', 34, 79],
                 index=df.columns, name=17)

df = df.append(john)

print(df)

df['js-score'] = np.array([71.0, 95.0, 88.0, 79.0, 91.0, 91.0, 80.0, 0])

print(df)

df['total-score'] = 0.0

print(df)

df.insert(loc=4, column='django-score',
          value=np.array([86.0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0, 2]))

print(df)

df = df.drop(labels='age', axis=1)

print(df)