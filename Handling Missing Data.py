import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

HPI_data = pd.read_pickle('../python_datasets/fmac_hpi_50_us_states.pkl')

HPI_data['TX1yr'] = HPI_data['TX'].resample('A').mean()
print(HPI_data[['TX', 'TX1yr']].head())

# .dropna() defaultly (how='any') removes all rows which contain NaN's
# DataFrame.dropna(inplace = True) is equal to DataFrame = DataFrame.dropna()
#HPI_data.dropna(inplace = True)

# .dropna(how='all') only drops rows,
# when all columns in this row contain Nan's
#HPI_data.dropna(how='all', inplace = True)

# DataFrame.fillna() value:fills NaN's with value
# limit: after reching limit, stops filling NaN's
HPI_data.fillna(value = 0, limit = 1000, inplace = True)

print(HPI_data[['TX', 'TX1yr']].head())

HPI_data[['TX', 'TX1yr']].plot(ax = ax1)


plt.legend(loc = 4)
plt.show()
