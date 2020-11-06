import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def recursiveDictPrint(seq, tabCount=0):
    print('\t'*tabCount, '{', sep='')
    for key in seq.keys():
        if isinstance(seq[key], dict):
            print('\t'*(tabCount+1), key + ':', sep='')
            recursiveDictPrint(seq[key], tabCount+1)
        else:
            print('\t'*(tabCount+1), key + ': ', seq[key], sep='')
    print('\t'*tabCount, '}', sep='')


def getAllData(towrite=False):
    if towrite:
        # Sending a GET query to WargamingAPI Centre with temporary access_token
        getURL = r"https://api.wotblitz.ru/wotb/account/info/?application_id=3e6fd2dd09b677081f667aa7d43a5578&account_id=42229071&access_token=2278d65eab9b08428bbbae04a3656d5ba565c9ec"
        content = {'key': '2278d65eab9b08428bbbae04a3656d5ba565c9ec', 'data': '42229071: statistics'}
        all_data = requests.get(getURL)
        all_data = all_data.json()
        # Writing json data to a file
        with open('account_info.txt', 'w') as fout:
            json.dump(all_data, fout)
    else:
        # Reading json data from a file which was saved once we have successfully received an answer on our GET query
        with open('account_info.txt', 'r') as fin:
            all_data = json.load(fin)
    return all_data


def getFragsData(towrite=False):
    frags_data = getAllData()
    frags_data = frags_data['data']['42229071']['statistics']['frags']
    if towrite:
        with open('frags.txt', 'w') as fout:
            json.dump(frags_data, fout)
    else:
        with open('frags.txt', 'r') as fin:
            frags_data = json.load(fin)
    return frags_data


def findZeros(seq):
    dictToReturn = {}
    for key in seq:
        if seq[key] == 0:
            dictToReturn.append((key, seq[key]))
    return dictToReturn


def getTankNameByID():
    df = pd.DataFrame()
    frags_data = getFragsData()
    _name = []
    _frags = []
    tankIDURL = r"https://api.wotblitz.ru/wotb/encyclopedia/vehicles/?application_id=3e6fd2dd09b677081f667aa7d43a5578"
    print('{:>3} {:>30} {:>5}'.format('ID', 'Tank Name', 'Frags'))
    tabooID_old = ['64081', '5441', '18689', '12545', '56609', '12033', '14337', '62017', '17153', '81', '3089', '545', '3329']
    # tabooId = ['64081', '81', '3089', '545', '3329', '609']
    tabooId = []
    index = 0
    for tankId in frags_data:
        headers = {'tank_id': tankId}
        result = requests.get(tankIDURL, headers=headers)
        result = result.json()
        if headers['tank_id'] in result['data']:
            tank_name = result['data'][headers['tank_id']]['name']
            print('{:>3} {:>30} {:>5}'.format(index, tank_name, frags_data[tankId]))
            index += 1
            _name.append(tank_name)
            _frags.append(frags_data[tankId])
        else:
            tabooId.append(headers['tank_id'])
    df['TankName'] = pd.Series(_name)
    df['Frags'] = pd.Series(_frags)
    with pd.ExcelWriter('frags_info.xlsx', mode='w') as eWriter:
        df.to_excel(eWriter)


def drawFragsPlot(showplot=True):
    df = pd.read_excel('frags_info.xlsx', usecols=['TankName', 'Frags'])
    df.sort_values(by='Frags', inplace=True)
    df.reset_index(inplace=True)

    # Draw plot
    plt.figure(figsize=(28, 60))
    plt.hlines(y=df.index, xmin=0, xmax=df['Frags'], linewidth=4)
    for x, y, tex in zip(df.Frags, df.index, df.Frags):
        t = plt.text(x+10, y, tex, horizontalalignment='right', verticalalignment='center')

    # Decorations
    plt.yticks(df.index, df['TankName'], fontsize=10)
    plt.title('Количество фрагов', fontdict={'size': 20})
    plt.xlim(0, max(df['Frags'])+15)
    if showplot:
        plt.show()
    # plt.savefig('frags.png', bbox_inches='tight')


def main():
    # print(json.dumps(getAllData(), indent=4))
    # print(json.dumps(getFragsData(), indent=4))
    # getTankNameByID()
    drawFragsPlot()


if __name__ == '__main__':
    main()

