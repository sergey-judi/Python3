import pandas as pd
import numpy as np


def answer_one():
    # Loading and processing the energy DataFrame
    energy_data = pd.read_excel(
        'Energy Indicators.xls',
        sheet_name='Energy',
        skiprows=17,
        usecols=[2, 3, 4, 5],
        index_col=2,
        skipfooter=283-245
    )
    energy_data.rename(columns={
        'Unnamed: 2': 'Country',
        'Petajoules': 'Energy Supply',
        'Gigajoules': 'Energy Supply per Capita',
        '%': '% Renewable'
        },
        inplace=True
    )
    energy_data['Energy Supply'] *= 1000000
    energy_data['Country'] = energy_data['Country'].str.replace(r' \(.*\)', '')
    energy_data['Country'] = energy_data['Country'].str.replace(r'\d+', '')
    energy_data.set_index(
        'Country',
        inplace=True
    )

    energy_data.rename(index={
        'Republic of Korea': 'South Korea',
        'United States of America': 'United States',
        'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
        'China, Hong Kong Special Administrative Region': 'Hong Kong'},
        inplace=True
    )

    # Loading and processing the GDP DataFrame
    cols_to_read = ['Country Name'] + [str(year) for year in range(1960, 2016)]
    GDP_data = pd.read_csv(
        'world_bank.csv',
        header=4,
        usecols=cols_to_read
    )
    GDP_data.rename(
        columns={'Country Name': 'Country'},
        inplace=True
    )

    ################################
    GDP_data['Country'] = GDP_data['Country'].str.replace(r'\(.*\)', '')
    GDP_data['Country'] = GDP_data['Country'].str.replace(r'\d+', '')
    ################################

    GDP_data.set_index(
        'Country', inplace=True
    )
    GDP_data.rename(
        index={
            'Korea, Rep.': 'South Korea',
            'Iran, Islamic Rep.': 'Iran',
            'Hong Kong SAR, China': 'Hong Kong'
        },
        inplace=True
    )

    ################################
    GDP_data.rename(
        index={
            "Republic of Korea": "South Korea",
            "United States of America": "United States",
            "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
            "China, Hong Kong Special Administrative Region": "Hong Kong"
        },
        inplace=True
    )
    ################################

    # Loading and processing the Sciamgo DataFrame
    ScimEn_data = pd.read_excel('scimagojr-3.xlsx')

    ################################
    ScimEn_data['Country'] = ScimEn_data['Country'].str.replace(r'\(.*\)', '')
    ScimEn_data['Country'] = ScimEn_data['Country'].str.replace(r'\d+', '')
    ################################

    ScimEn_data.set_index('Country', inplace=True)
    ScimEn_data.rename(
        index={
            "Republic of Korea": "South Korea",
            "United States of America": "United States",
            "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
            "China, Hong Kong Special Administrative Region": "Hong Kong"
        },
        inplace=True
    )

    #  Merging three DataFrames
    cols_to_merge = [str(col) for col in range(2006, 2016)]
    GDP_data = GDP_data[cols_to_merge]

    merged = pd.merge(ScimEn_data, energy_data, how='inner', on='Country')
    merged = pd.merge(merged, GDP_data, how='inner', on='Country')
    merged = merged.sort_values(by='Rank')

    # with pd.ExcelWriter('A1.xlsx', mode='w') as eWriter:
    #  energy_data.to_excel(eWriter)
    # with pd.ExcelWriter('A2.xlsx', mode='w') as eWriter:
    #  GDP_data.to_excel(eWriter)
    # with pd.ExcelWriter('A3.xlsx', mode='w') as eWriter:
    #  ScimEn_data.to_excel(eWriter)
    #
    # with pd.ExcelWriter('A_RESULT.xlsx', mode='w') as eWriter:
    #  merged.iloc[:15, :20].to_excel(eWriter)
    # print(sorted(energy_data.index.to_list()))
    # print(sorted(GDP_data.index.to_list()))
    # print(sorted(ScimEn_data.index.to_list()))
    #  return first 15 rows and 20 columns
    return merged.iloc[:15, :20]


def answer_two():
    # Loading and processing the energy DataFrame
    energy_data = pd.read_excel(
        'Energy Indicators.xls',
        sheet_name='Energy',
        skiprows=17,
        usecols=[2, 3, 4, 5],
        index_col=2,
        skipfooter=283 - 245
    )
    energy_data.rename(columns={
        'Unnamed: 2': 'Country',
        'Petajoules': 'Energy Supply',
        'Gigajoules': 'Energy Supply per Capita',
        '%': '% Renewable'
    },
        inplace=True
    )
    energy_data['Energy Supply'] *= 1000000
    energy_data['Country'] = energy_data['Country'].str.replace(r' \(.*\)', '')
    energy_data['Country'] = energy_data['Country'].str.replace(r'\d+', '')
    energy_data.set_index(
        'Country',
        inplace=True
    )

    energy_data.rename(index={
        'Republic of Korea': 'South Korea',
        'United States of America': 'United States',
        'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
        'China, Hong Kong Special Administrative Region': 'Hong Kong'},
        inplace=True
    )

    # Loading and processing the GDP DataFrame
    cols_to_read = ['Country Name'] + [str(year) for year in range(1960, 2016)]
    GDP_data = pd.read_csv(
        'world_bank.csv',
        header=4,
        usecols=cols_to_read
    )
    GDP_data.rename(
        columns={'Country Name': 'Country'},
        inplace=True
    )

    ################################
    GDP_data['Country'] = GDP_data['Country'].str.replace(r'\(.*\)', '')
    GDP_data['Country'] = GDP_data['Country'].str.replace(r'\d+', '')
    ################################

    GDP_data.set_index(
        'Country', inplace=True
    )
    GDP_data.rename(
        index={
            'Korea, Rep.': 'South Korea',
            'Iran, Islamic Rep.': 'Iran',
            'Hong Kong SAR, China': 'Hong Kong'
        },
        inplace=True
    )

    ################################
    GDP_data.rename(
        index={
            "Republic of Korea": "South Korea",
            "United States of America": "United States",
            "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
            "China, Hong Kong Special Administrative Region": "Hong Kong"
        },
        inplace=True
    )
    ################################

    # Loading and processing the Sciamgo DataFrame
    ScimEn_data = pd.read_excel('scimagojr-3.xlsx')

    ################################
    ScimEn_data['Country'] = ScimEn_data['Country'].str.replace(r'\(.*\)', '')
    ScimEn_data['Country'] = ScimEn_data['Country'].str.replace(r'\d+', '')
    ################################

    ScimEn_data.set_index('Country', inplace=True)
    ScimEn_data.rename(
        index={
            "Republic of Korea": "South Korea",
            "United States of America": "United States",
            "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
            "China, Hong Kong Special Administrative Region": "Hong Kong"
        },
        inplace=True
    )

    #  Merging three DataFrames
    cols_to_merge = [str(col) for col in range(2006, 2016)]
    GDP_data = GDP_data[cols_to_merge]

    merged = pd.merge(ScimEn_data, energy_data, how='inner', on='Country')
    merged = pd.merge(merged, GDP_data, how='inner', on='Country')

    diff1 = pd.merge(ScimEn_data, energy_data, how='outer', on='Country')
    diff2 = pd.merge(diff1, GDP_data, how='outer', on='Country')

    return diff2.shape[0] - merged.shape[0]


def avg(row):
    cols = [str(year) for year in range(2006, 2016)]
    data = row[cols]
    divider = 10
    if row.name == 'Iran':
        divider = 9
    row['avgGDP'] = np.sum(data) / divider
    return row


def answer_three():
    Top15 = answer_one()
    Top15.fillna(0, inplace=True)
    Top15 = Top15.apply(avg, axis=1)
    Top15.sort_values(by='avgGDP', inplace=True, ascending=False)
    return Top15['avgGDP']


def answer_four():
    Top15 = answer_one()
    return Top15.loc['United Kingdom']['2015'] - Top15.loc['United Kingdom']['2006']


def answer_five():
    Top15 = answer_one()
    return np.mean(Top15['Energy Supply per Capita'])


def answer_six():
    Top15 = answer_one()
    countryName = Top15['% Renewable'].argmax()
    return countryName, Top15.loc[countryName]['% Renewable']


def answer_seven():
    Top15 = answer_one()
    Top15['Ratio'] = (Top15['Self-citations'])/(Top15['Citations'])
    countryName = Top15['Ratio'].argmax()
    return (countryName, Top15.loc[countryName]['Ratio'])


def answer_eight():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15.sort_values(by='Population', ascending=False,inplace=True)
    return Top15.iloc[2].name


def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15['Citable docs per Capita'] = np.float64(Top15['Citable docs per Capita'])
    Top15['Energy Supply per Capita'] = np.float64(Top15['Energy Supply per Capita'])
    return Top15['Energy Supply per Capita'].corr(Top15['Citable docs per Capita'])


Top15 = answer_one()
median = float(np.median(Top15['% Renewable']))
def greaterThanMedian(row):
    data = row['% Renewable']
    row['HighRenew'] = 1 if data > median else 0
    return row


def answer_ten():
    global Top15
    Top15 = Top15.apply(greaterThanMedian, axis=1)
    return Top15['HighRenew']


