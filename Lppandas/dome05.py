import pandas as pd
import numpy as np
import openpyxl
import xlrd

ts = pd.Series(np.random.randn(10), index=pd.date_range('1/1/2000', periods=10))

df = pd.DataFrame(np.random.randn(10, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])

# df.to_csv('foo.csv')

print(pd.read_csv('foo.csv'))

# df.to_hdf('foo.h5', 'df')
#
# print(pd.read_hdf('foo.h5', 'df'))


# df.to_excel('foo.xlsx', sheet_name='Sheet1')
#
# print(pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA']))

