import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(')  # split the index by '('

df.index = names_ids.str[0]  # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3]  # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')


def answer_one():
    return df['Gold'].argmax()


def answer_two():
    return abs(df['Gold'] - df['Gold.1']).argmax()


def answer_three():
    return (df[(df['Gold'] >= 1) & (df['Gold.1'] >= 1)]['Gold'] -
             df[(df['Gold'] >= 1) & (df['Gold.1'] >= 1)]['Gold.1']
             )/(
            df[(df['Gold'] >= 1) & (df['Gold.1'] >= 1)]['Gold'] +
            df[(df['Gold'] >= 1) & (df['Gold.1'] >= 1)]['Gold.1'] +
            df[(df['Gold'] >= 1) & (df['Gold.1'] >= 1)]['Gold.2']
    ).argmax()


def answer_four():
    return pd.Series(df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2'], index=df.index, name='Points')


print(answer_one())
print(answer_two())
print(answer_three())
print(answer_four())
