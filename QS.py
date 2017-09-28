# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 05:22:04 2016

@author: Waleed
"""
#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook 


def plot(b):
 x = [x for x in range(len(b))]
 plt.figure()
 plt.bar(x, b)
 plt.xlabel('n')
 plt.ylabel('range')
 plt.title('Quick Sort')
 plt.show()
 plt.clf


def part(a,beg,lst):
    #set pivot to the last element
    pvt = a[lst]
    #set index to the begining of the array
    index = beg
    #current index is at the begining
    curind = beg
    
    while (curind <lst):
        #if the element of the current ind is less than pivot swap 
     if(a[curind] <= pvt):
         a[index], a[curind] = a[curind], a[index]
        #increment index
         index+=1
     curind +=1
    a[index], a[lst] = a[lst], a[index]
    #plot sorting algorithm
    plot(a)
    print('.')
    return index
    
def QS(a,beg,lst):
    if (beg<lst):
        index = part(a,beg,lst)
        #recursive calls to quicksort for first and second half
        QS(a,beg,index-1)
        QS(a,index+1,lst)
        
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
  
        


QS(a,0,49)
     
    