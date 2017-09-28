# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 01:14:24 2016

@author: Waleed
"""
#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook 


        
a = [0.420537845,
-0.666325377,
0.042048214,
1.469388735,
0.425725375,
-0.591544449,
-0.616147418,
-0.130454509,
-1.943608368,
0.544706609,
0.348696858,
0.780023584,
-0.026968792,
0.236619826,
-1.144126145,
1.462217369,
-2.285578375,
0.61198989,
1.135047114,
-0.125750148,
0.02138222,
-1.80595634,
0.258627324,
-0.863337846,
1.001092187,
-0.727876568,
0.641880433,
0.309447614,
1.550947673,
-1.300154508,
0.774848559,
-0.546569936,
-0.06280743,
-1.627167876,
0.295433438,
0.075231128,
2.48041033,
-0.21824917,
1.603480086,
0.840684606,
1.306054855,
-1.767830327,
-0.135703431,
0.957595603,
-0.709947017,
0.452175755,
1.025507572,
-2.195356501,
0.210578719,
0.80093514]  

def plot(b):
 x = [x for x in range(len(b))]
 plt.figure()
 plt.bar(x, b)
 plt.xlabel('n')
 plt.ylabel('range')
 plt.title('Selection Sort')
 plt.show()
 
 

def SelectionSort(a):
    for i in range (0,len(a) - 1):
        minInd = i
        for j in range (i+1, len(a)):
            #if the current minimum index value greater than current j'th
            #set minimum index to the current j'th index
            if a[j] < a[minInd]:
                minInd = j
        #Now if the minimum index is not equal to i then swap
        if minInd != i:
            a[i], a[minInd] = a[minInd],a[i]
        plot(a)
        print('.')
        
      
SelectionSort(a)
