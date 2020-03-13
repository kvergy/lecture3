#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import os

n = int(sys.argv[1])
seq = ''

dicti = []
first = []
last = []
middle = []
count = []
"""
for path in sys.stdin:
with open(path.strip()) as inf:"""
#with open('/home/kvergy/Downloads/sample.fasta') as inf:
#for path in sys.stdin:
with open(sys.argv[2]) as inf:
    file = inf.read().split('\n')
    for row in file[1:]:
        seq += row
            
i = 0
k = 0
while i < (len(seq) - n):

    if seq[i:i+n] not in dicti:
        dicti.append(seq[i:i+n])
        first.append(i)
        middle.append(i)
        last.append(i)
        count.append(1)
        
    else:
        num = dicti.index(seq[i:i+n])
        middle[num] += i
        last[num] = i
        count[num] += 1
    i += 1    
print('kmer   ', 'first index  ', 'middle index  ', 'last index  ', 'num')      
for k in range(len(dicti)):
    print(dicti[k],'  ',first[k],'  ', "%.2f" % (middle[k]/count[k]),'  ', last[k],'  ', count[k])
        
        
    
    

