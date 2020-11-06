import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cols_to_use = [_ for _ in range(3, 16)]

# for level in range(1, 3):
#     df = pd.read_excel('data_tank.xlsx', usecols=cols_to_use)
#     df = df[df['Уровень'] == level]
#     df = df[['Название', 'Кол-во']]
#     df.set_index('Название', inplace=True)
#     df.sort_values(by='Кол-во', inplace=True)
#     df.plot(kind='barh', figsize=(8, 15))
#     plt.savefig('tier' + str(level) + '.png', bbox_inches='tight', dpi=1200)
#     plt.show()

SHOWPLOT = False
for lvl in range(1, 11):
    df = pd.read_excel('data_tank.xlsx', usecols=cols_to_use)
    df = df[df['Уровень'] == lvl]
    df = df[['Название', 'Кол-во']]
    df.sort_values(by='Кол-во', inplace=True)
    df.rename(columns={"Название": "tankName", "Кол-во": "tankAmount"}, inplace=True)
    df.reset_index(inplace=True)

    # Draw plot
    plt.figure(figsize=(20, 20))
    plt.hlines(y=df.index, xmin=0, xmax=df['tankAmount'])
    for x, y, tex in zip(df.tankAmount, df.index, df.tankAmount):
        t = plt.text(x + 3000, y, tex, horizontalalignment='right', verticalalignment='center')

    # Decorations
    plt.yticks(df.index, df['tankName'], fontsize=12)
    plt.title('Количество танков в игре', fontdict={'size':20})
    plt.xlim(0, max(df['tankAmount']) + 3500)
    plt.savefig('tier' + str(lvl) + '.png', bbox_inches='tight', dpi=800)
    if SHOWPLOT:
        plt.show()
    print('Successfully created tier' + str(lvl) + '.png file.')

