import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

HPI_data = pd.read_pickle('../python_datasets/fmac_hpi_50_us_states.pkl')

'''Documentation for resampling 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html

Parameter list for .resample('Parameter') 
https://stackoverflow.com/questions/17001389/pandas-resample-documentation'''

TX1yr = HPI_data['TX'].resample('A').mean()
print(TX1yr.head())

HPI_data['TX'].plot(ax = ax1, label = 'Monthly TX HPI')
TX1yr.plot(ax = ax1, label = 'Yearly TX HPI')

plt.legend(loc = 4)
plt.show()
