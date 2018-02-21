# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 06:16:13 2016

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
 plt.title('Merge Sort')
 plt.show()
 plt.clf

def MS(a):
    if len(a)<=1:
        return a
    #Divide pat of the algorithm it divides the array to two halfs
    mid = int(len(a)/2)
    left = MS(a[:mid])
    right = MS(a[mid:])
    #merge right and left subarray
    return merge(left,right)
    
#Merge function
def merge(left, right):
    result = []
    #while there are elements in the left and right sub arrays
    while len(left) > 0 and len(right) > 0:
        #if the left most element of the left array is smaller than that of the right append left
        #else append right
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left)>0:
        result += left
    if len(right) > 0:
        result += right
    print('.')
    #plotting function, defined above
    plot(result)    
    #return the merged subarrays
    return result
    
#array of randomly generated data points   
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


B = MS(a)
