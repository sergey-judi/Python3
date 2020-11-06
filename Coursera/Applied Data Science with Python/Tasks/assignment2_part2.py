import pandas as pd

census_df = pd.read_csv('census.csv')


def answer_five():
    df = census_df[census_df['SUMLEV'] == 50]
    df = df.set_index(['STNAME'])
    unique_states = sorted(set(df.index))
    state_df = pd.DataFrame()
    state_df['STATE'] = unique_states
    state_df['COUNT'] = 0
    state_df = state_df.set_index(['STATE'])
    for state in state_df.index:
        stcount = len(df.loc[state])
        state_df['COUNT'].loc[state] = stcount
    return unique_states[state_df['COUNT'].argmax()]


def answer_six():
    df = census_df[census_df['SUMLEV'] == 50]
    df = df.set_index(['STNAME'])
    unique_states = sorted(set(df.index))
    state_df = pd.DataFrame()
    state_df['STATE'] = unique_states
    state_df['POPULATION'] = 0
    print(df.sum(axis=0))
    for state in state_df.index:
        print(df.loc[state].sum()['CENSUS2010POP'])
        #stcount = df.loc[state].sum()['CENSUS2010POP']
        #state_df['POPULATION'].loc[state] = stcount
    #print(state_df)
    # colsToStay = ['COUNTY', 'STNAME', 'CENSUS2010POP']
    # temp = census_df[census_df['SUMLEV'] == 50]
    # temp = temp.set_index('CENSUS2010POP')
    # temp = temp.sort_index(ascending=False)
    # return temp[:3]['STNAME'].to_list()

def answer_seven():
    popcols = ["POPESTIMATE20" + str(x) for x in range(10, 16)]
    cols = ['SUMLEV', 'CTYNAME'] + popcols
    dfp = census_df[cols]
    dfp = dfp[dfp['SUMLEV'] == 50]
    dfp = dfp.set_index('CTYNAME')
    maxx = dfp[popcols].max(axis=1)
    minn = dfp[popcols].min(axis=1)
    dfp['diff'] = abs(maxx - minn)
    #  census_df.iloc[dfp['diff'].argmax()]['CTYNAME']
    return census_df.iloc[dfp['diff'].argmax()]['CTYNAME']


def answer_eight():
    dfp = census_df[
        (census_df['REGION'] == 1) |
        (census_df['REGION'] == 2) &
        (census_df['SUMLEV'] == 50)
        ]
    dfp = dfp[dfp['CTYNAME'].str.startswith('Washington')]
    dfp = dfp[dfp['POPESTIMATE2015'] > dfp['POPESTIMATE2014']]
    dfp = dfp[['STNAME', 'CTYNAME']]
    return dfp


#print(answer_five())
print(answer_six())
#print(answer_seven())
#print(answer_eight())


