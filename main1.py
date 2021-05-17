import pandas as pd
import numpy as np
from Expiry_map import expiry_map

# data15 = pd.read_csv("apr15.csv")
data16 = pd.read_csv("apr16.csv")
data18 = pd.read_csv("apr18.csv")
data19 = pd.read_csv("apr19.csv")

# data15.columns =['Datetime', 'Open', 'High', 'Low', 'Close', 'OI']
data16.columns =['Datetime', 'Open', 'High', 'Low', 'Close', 'OI']
data18.columns =['Datetime', 'Open', 'High', 'Low', 'Close', 'OI']
data19.columns =['Datetime', 'Open', 'High', 'Low', 'Close', 'OI', 'NON']
data19 = data19.drop(['NON'], axis=1)

all_dataFrames=[ data16, data18, data19]
data = pd.concat(all_dataFrames, ignore_index=True)

data = data.sort_values(by=['Datetime'], ascending=True)
data.set_index("Datetime")

# print(data.head)
# print(data.describe())

# data.drop( data[ data['Datetime'][0:4] == '2015' ].index , inplace=True)

finaldataframe=[]

lastcurrent=0
for dict in range(len(expiry_map)-1):
    current1 = expiry_map[dict]['expiry']
    current1 = int(current1[0:4] + current1[5:7] + current1[8:10])
    current2 = expiry_map[dict+1]['expiry']
    current2 = int(current2[0:4] + current2[5:7] + current2[8:10])
    lastcurrent=current2
    dataframe = []
    for index, row in data.iterrows():
        current=int(row['Datetime'][0:4]+row['Datetime'][5:7]+row['Datetime'][8:10])

        if current1 < current and current2 >= current:
            dataframe.append(row)
    df = pd.DataFrame(dataframe)
    finaldataframe.append(df)

dataframe = []
for index, row in data.iterrows():
    current=int(row['Datetime'][0:4]+row['Datetime'][5:7]+row['Datetime'][8:10])
    if lastcurrent <current:
        dataframe.append(row)
df = pd.DataFrame(dataframe)
finaldataframe.append(df)




for d in finaldataframe:
    print(d.to_string(index=False))
    print()
    print()
    print()
    print()