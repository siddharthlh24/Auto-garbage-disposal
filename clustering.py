import numpy as np
from matplotlib import pyplot as plt
import random
import random
import math
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
import time
#from mayavi import mlab
count=0
df = pd.read_csv('doctored_2.csv',)
newarr = df.to_numpy()
#print(newarr.shape)
"""fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
pnt3d = ax.scatter(newarr[0],newarr[1],newarr[2],c=newarr[2])
cbar=plt.colorbar(pnt3d)"""

km = KMeans(n_clusters=4, random_state=0).fit(newarr[2].reshape(-1,1))
predarray = newarr[2]

clusters = (km.predict(predarray.reshape(-1,1)))
#print(clusters)

#print(km.cluster_centers_)

newarr = np.vstack([newarr,clusters])
#print(newarr)

"""for i in range(len(newarr[3])):
    newarr[3][i] = km.cluster_centers_[newarr[3][i]][0]"""

newtran = np.transpose(newarr)

# print(newtran)

arr = newtran[newtran[:,3].argsort()]

#print(arr)

plotarr = np.array([0,0,0,0])
plotarrq=plotarr

fig = plt.figure()


ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('latititude')
ax.set_ylabel('longitude')
ax.set_zlabel('time in hours')

plt.ion()


for i in range(len(km.cluster_centers_)):
    for j in range(len(newarr[3])):
        if((arr[j][3]==i)):
             plotarr = np.vstack([plotarr, (arr[j]) ])
             plotarrq = np.vstack([plotarrq, (arr[j]) ])
        #plotarr = np.vstack([plotarr, (arr[np.where(arr[j][3]==i)]) ])
    if(i==0):
        old = plotarr
    #plottranx =  np.array(set(plotarr).symmetric_difference(old))  
    plottran = np.transpose(plotarr)
    plottranq= np.transpose(plotarrq)



    print(plottranq)
    #pnt3d = 
    ax.scatter(plottran[0],plottran[1],plottran[2],c=plottran[2])
    #cbar=plt.colorbar(pnt3d)

    namex = str(count)+".csv"
    df = pd.DataFrame(plottranq)
    df.to_csv(namex, mode='w',index=False)
    count=count+1

    plt.draw()
    plt.pause(1)
    plotarr = np.transpose(plottran)
    plotarrq = np.array([0,0,0,0])


plt.pause(1000)
plt.show()
