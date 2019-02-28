import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

#Not necessary, I just do this so I do not show my API key.
api_key = open('../quandl_api_key.txt', 'r').read()

#Imports a list of all us states from wikipedia html
def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0]['Name &postal abbreviation[1]']['Name &postal abbreviation[1].1']

#Serializes the list of us states in a pkl file locally
#state_list().to_pickle('python_datasets/list_of_us_states.pkl')

#Loads local pkl file which contains a list of all us states
#df_us_states = pd.read_pickle('python_datasets/list_of_us_states.pkl')

def grab_initial_state_data_nsa_sa():
    states = state_list()
    main_df = pd.DataFrame()
    
    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        df = quandl.get(query, authtoken = api_key)
        nsa = str(abbv) + ' NSA Value'
        sa = str(abbv) + ' SA Value'
        df.rename(columns={'NSA Value': nsa, 'SA Value' : sa}, inplace=True)
        df[nsa] = (df[nsa] - df[nsa][0]) / df[nsa][0] * 100.0
        df[sa] = (df[sa] - df[sa][0]) / df[sa][0] * 100.0
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    main_df.to_pickle('../python_datasets/fmac_hpi_nsa_sa_50_us_states.pkl')

def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()
    
    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        df = quandl.get(query, authtoken = api_key)
        df = df.drop('SA Value', axis = 1)
        df.rename(columns={'NSA Value': str(abbv)}, inplace=True)
        df[str(abbv)] = (df[str(abbv)] - df[str(abbv)][0]) / df[str(abbv)][0] * 100.0
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    main_df.to_pickle('../python_datasets/fmac_hpi_50_us_states.pkl')
    
def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken = api_key)
    usa = 'United States'
    df = df.drop('SA Value', axis = 1)
    df.rename(columns={'NSA Value': usa}, inplace=True)
    df[usa] = (df[usa] - df[usa][0]) / df[usa][0] * 100.0
    return df

#grab_initial_state_data()

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))


HPI_data = pd.read_pickle('../python_datasets/fmac_hpi_50_us_states.pkl')
benchmark = HPI_Benchmark()

HPI_data.plot(ax = ax1)
benchmark.plot(ax = ax1, color='k', linewidth = 10)

plt.legend().remove()
plt.show()


