import random

import pandas as pd
from random import choice
from random import randint
from random import shuffle
from datetime import date

#the amount of noise generated in %
noise_level=10


valid_data = 'C:/Users/vince/Desktop/Studium/Thesis/FB15K-237.2/Release/valid.txt'
data = pd.read_csv(valid_data, sep='\t', header=None)
data.columns=["head","relation","tail"]
rows=(len(data.index))

#select random relations where nodes will be modified
acceptor_triples=[]
temp=list(range(rows))
random.shuffle(temp)
for x in range(int(rows*noise_level*0.01)):
    acceptor_triples.append(temp.pop(0))
print(acceptor_triples)

#select donor nodes from disjoint set of relations
donor_triples=[]
for x in range(int(rows*noise_level*0.01)):
    donor_triples.append(temp.pop(0))
print(donor_triples)
printed_progress=''

#randomly select a head or tail node to be altered
for x in range(len(donor_triples)):
    head_or_tail=randint(0,1)
    progress=int(x/len(donor_triples)*100)
    if(progress!=printed_progress):
        print(str(progress)+'%')
        printed_progress=progress
    if(head_or_tail==0):
        data['head'][acceptor_triples[x]]=data['head'][donor_triples[x]]
    else:
        data['tail'][acceptor_triples[x]]=data['tail'][donor_triples[x]]

print(data.head())
outputfile='fb15k-237_valid'+'_noise_'+str(noise_level)+'.txt'
data.to_csv(outputfile,sep='\t',header=False,index=False)