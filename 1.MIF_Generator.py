import numpy as np
import pandas as pd
import random
import json

InputFile = pd.read_csv("data.csv", header=None)
rows = len(InputFile)
nOriginal = 1000
nTilde = 10

InputMatrix = InputFile.to_numpy()
RefIndices = random.sample(range(1, rows+1),nOriginal)
json.dump(RefIndices, open ('RefIndices.json', 'w'))

def PrunedRef(obj):
    Diff = abs(InputMatrix[obj] - InputMatrix[RefIndices])
    Dist = Diff.sum(axis = 1)
    DistMatrix = np.array(Dist)
    SortRefIndices = np.argsort(DistMatrix)
    PrunedRefIndices = SortRefIndices[0:nTilde:1]
    return PrunedRefIndices

RefObjList = np.array([PrunedRef(0)])
for n in range(len(InputMatrix)-1):
    y = np.append(RefObjList, [PrunedRef(n+1)],axis=0)
    RefObjList = y
    
MIFDict = {}
temp = []
for i in range(rows):
    for j in range(nTilde):
        KeyItem = RefObjList[i][j]
        ItemThere = MIFDict.get(KeyItem)
        if ItemThere:
            CurrentMIF = MIFDict.get(KeyItem)
            CurrentMIFTouple = (i,j)
            CurrentMIF.append(CurrentMIFTouple)
            MIFDict[int(KeyItem)] = CurrentMIF
        else:
            CurrentMIFTouple = (i,j)
            temp = []
            temp.append(CurrentMIFTouple)
            MIFDict[int(KeyItem)] = temp
#print(MIFDict)

json.dump(MIFDict, open ('MIFFile.json', 'w'))