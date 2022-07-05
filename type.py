import random

import numpy.random
import pandas as pd
import numpy as np
from random import choice
from random import randint
from random import shuffle
from datetime import date

# the amount of noise generated in %
noise_level = 10

#training_data = 'C:/Users/vince/Desktop/Studium/Thesis/FB15K-237.2/Release/train.txt'
training_data = "C:/Users/vince/Desktop/test/train.txt"

data = pd.read_csv(training_data, sep='\t', header=None)
data.columns = ["head", "relation", "tail"]
rows = (len(data.index))
uniqueRelations = np.array(data.relation.unique())
typeRegistry = {}
# data['type']="nan"
for index, row in data.iterrows():
    same_type = np.where(uniqueRelations == row.relation)[0]
    current_type = same_type[0]
    # data['type'][index]=current_type
    print(index)
    indices = typeRegistry.get(current_type, [])
    indices.append(index)
    typeRegistry.update({current_type: indices})
i = 0
modified_triple = []
while i < int(rows * noise_level * 0.01):
    randType = numpy.random.randint(len(typeRegistry.keys()))
    typeArray = typeRegistry.get(randType)
    if (len(typeArray) < 2):
        continue
    random.shuffle(typeArray)
    head_or_tail = numpy.random.randint(low=0, high=2)
    if (typeArray[0] in modified_triple):
        continue
    if (head_or_tail == 0):
        data['head'][typeArray[0]] = data['head'][typeArray[1]]
    else:
        data['tail'][typeArray[0]] = data['tail'][typeArray[1]]
    modified_triple.append(typeArray[0])
    i += 1
    print("Modified: " + str(typeArray[0]))

"""
uniqueRelColumn=[]
for x in uniqueRelations:
    uniqueRelColumn.append(x+"_head")
    uniqueRelColumn.append(x + "_tail")
    
print(data.head())
typeRegistry=pd.DataFrame(columns=uniqueRelations)
print(typeRegistry.head())
for index, row in data.iterrows():
    if index==0:
        typeRegistry.loc[0, row.relation] = index
    print(index)
    while not(typeRegistry.loc[i, row.relation=='nan']):
        i+=1
    typeRegistry.loc[i,row.relation]=index
    i+=1
    """
print('done')
outputfile='fb15k-237_train'+'_noise_'+str(noise_level)+'_type_test.txt'
data.to_csv(outputfile,sep='\t',header=False,index=False)
