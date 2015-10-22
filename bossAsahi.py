import matplotlib.pyplot as plt
import json
import numpy as np
import random
import kMeans
import sys, os, bonglib
from bonglib import pause
import time

init_time = time.time()



'''Magic Numbers'''
FILENAME = sys.argv[1]
nLOOP = 500
K = 20
min_X = 122.286; max_X = 133; min_Y = 32.85; max_Y = 39
#min_X = 124; min_Y = 3; max_Y = 39; max_X = 130

'''Initial settings for matplotlib.pyplot'''
plt.axis([min_X, max_X, min_Y, max_Y])
plt.ylabel('hotels')



def randMarker():
	colors = ['g', 'c', 'm', 'y']
	shapes = ['^', 's', 'p', '*', 'h', 'p', 'o', 'v']
	return random.choice(colors) + random.choice(shapes)


def loadDataSet(filename):
        dataList = []
        target_file = (json.loads(open(filename, 'r').read())) # Open target JSON file
        for line in target_file:
        	if line['country_region_id'] == 94:
        		if line['longitude'] > 125 and line['longitude'] < 140 and line['latitude'] > 30 and line['latitude'] < 40:
        			floatized = list(map(float,[line['longitude'], line['latitude']]))
        			floatized.insert(0,line['id'])
        			dataList.append(floatized)


        	else:
        		pass
        dataMat = np.mat(dataList) # Convert dataList to Matrix(numpy expression)
        return dataMat

def setPlot(dataMat, shape):
	axisX = []
	axisY = []
	if dataMat[0].shape[1] == 3:
		for s in dataMat:
			axisX.append(s[0, 1])
			axisY.append(s[0, 2])

	else:
		for s in dataMat:
			axisX.append(s[0, 0])
			axisY.append(s[0, 1])

	plt.plot(axisX, axisY, shape)
	
	
hotelcolor = randMarker()
Indexed_DataMat = loadDataSet(FILENAME)	






firstcent = (kMeans.randomCents(Indexed_DataMat, K))

def Recursive_kMeans(centroids, dataMat, K, loop):
	global nLOOP
	if loop > 0:
		loop -= 1
		print("Recursive kMeans Loop: %d times" %(nLOOP - loop))
		new_centroids = kMeans.kMeans(centroids["centroids"], dataMat, K)

		return Recursive_kMeans(new_centroids, dataMat, K, loop)
	else:
		print("Recursive kMeans Loop: Finished.")
		return centroids

#print (Recursive_kMeans(firstcent, Indexed_DataMat, K, nLOOP))


print (firstcent)
print (kMeans.kMeans(firstcent, Indexed_DataMat, K))

setPlot((Indexed_DataMat), hotelcolor)
setPlot(firstcent, 'b+')
plt.show()


plt.axis([min_X, max_X, min_Y, max_Y])
plt.ylabel('hotels')
setPlot((Indexed_DataMat), hotelcolor)

loadedfirstcent = {"centroids": firstcent}

setPlot(Recursive_kMeans(loadedfirstcent, Indexed_DataMat, K, nLOOP)["centroids"], 'r+')
plt.show()
