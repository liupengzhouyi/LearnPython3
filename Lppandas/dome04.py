import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(10), index=pd.date_range('1/1/2000', periods=10))

ts = ts.cumsum()

ts.plot()

plt.show()




df = pd.DataFrame(np.random.randn(10, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])

plt.figure()

df.plot()

plt.legend(loc='best')

plt.show()