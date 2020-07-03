import numpy as np
from matplotlib import pyplot as plt
import random
import random
import math
import pandas as pd

import pandas as pd


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def bubbleSort(arr,arrx,arry):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                arrx[j], arrx[j+1] = arrx[j+1], arrx[j]
                arry[j], arry[j+1] = arry[j+1], arry[j]

"""y = np.array([])
x = np.array([])

x = random.sample(range(1, 100), 20)
y = random.sample(range(1, 100), 20)"""

df = pd.read_csv('doctored_2.csv',)
newarr = df.to_numpy()

x = newarr[0]
y = newarr[1]

plt.plot(x,y,'ro')

"""dbpts = np.array([])\
dbpts = random.sample(range(0, 16), 10)"""
count=0
while(count<4):
    yp = np.array([])
    xp = np.array([])

    name = str(count) + ".csv"
    df = pd.read_csv(name,)
    count=count+1
    newarrz = df.to_numpy()
    newtranv = np.transpose(newarrz)

    lflx = 0
    lfly = 0

    """xp  =np.append(xp,[lflx])        #landfill location, also starting point
    yp  =np.append(yp,[lfly])"""

    xp = newarrz[0]
    yp = newarrz[1]

    maxval = np.max(newarrz[2])

    cx = np.mean(xp)        #centroid
    cy = np.mean(yp)

    print(xp)
    print(yp)

    print(cx,cy)

    #plt.plot(cx,cy, marker='o', markersize=7, color="black")      #centroid plot
    plt.plot(xp,yp,'bo')
    hours = "at " + str(maxval) + " hours"
    #fig = plt.figure()
    plt.suptitle(hours)
    plt.xlabel('latitude')
    plt.ylabel('longitude')
    #plt.plot(xp,yp,'g')

    tanvals = np.array([])
    tanvals = np.append(tanvals,np.arctan2((yp-cy),(xp-cx)))
    #tanvals = np.degrees(np.arctan(tanvals))
    #print(tanvals)

    lflang = tanvals[len(tanvals)-1]
    print(lflang)
    #print(xp)
    #print(yp)



    bubbleSort(tanvals,xp,yp)
    print(tanvals)

    index = np.where(tanvals==lflang)
    indexk = index[0][0]
    print(indexk)

    xp=np.roll(xp,-indexk,0)
    yp=np.roll(yp,-indexk,0)
    tanvals=np.roll(tanvals,-indexk,0)


    print(tanvals)
    plt.plot(x,y,'ro')
    plt.plot(xp,yp,'b')
    plt.show()

    #print(tanvals)
    #print(xp)
    #print(yp)

