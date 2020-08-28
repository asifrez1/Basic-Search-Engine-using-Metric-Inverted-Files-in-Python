print('Initializing...\n')

print("If you haven't already, Please enter your query in the 'Enter_Query_Here.csv' file in the local directory \n" )

import json
import numpy as np
import pandas as pd
import datetime

start = datetime.datetime.now()

QueryItem = pd.read_csv('Enter_Query_Here.csv',header = None)
MIFFile = json.load(open('MIFFile.json'))
DataFile = pd.read_csv('data.csv',header = None)
Ref = json.load(open('RefIndices.json'))
RefFile = pd.DataFrame(Ref).T
row, nRef = RefFile.shape

print('Your Query Object \n', list(QueryItem.loc[0,:]), '\n')

def DistanceF(x, y):
    temp = 0
    for i in range(len(x)):
        temp = temp + abs (x[i]-y[i])
    return temp

QueryRefDistance = []
for j in range(nRef):
    QueryRefDistance.append(int(DistanceF(QueryItem.loc[0,:],DataFile.loc[RefFile[j],:])))
    
DistanceSorted = np.argsort(QueryRefDistance)
Dic_DistanceSorted = {}
for i in DistanceSorted:
    Dic_DistanceSorted[i] = MIFFile[str(DistanceSorted[i])]

SearchResult = []
counter = 0

for values in Dic_DistanceSorted.values():
    if (counter == 20):
        break
    for item in values:
        if (item[1] == 0):
            SearchResult.append(item[0])
            counter = counter + 1
            if (counter == 20):
                break

print('Indices of the Similar Objects \n', SearchResult, '\n')

print('Loading Similar Objects...\n')

for i in range(len(SearchResult)):
    print('Similar Object #',i, '\n', list(DataFile.loc[SearchResult[i],:]))

end = datetime.datetime.now()
print('\n')
print('20 Similar Objects Returned in', end-start, 'seconds')