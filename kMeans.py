import numpy as np
import random
from bonglib import pause, dpause
import matplotlib.pyplot as pl
from scipy.spatial.distance import cosine



#define
Inf = np.inf



def randomCents(dataMat, k):
	num = np.shape(dataMat)[1] - 1
	centroids = np.mat(np.zeros((k, num)))
	for p in range(num):
		minimumPos = min(dataMat[:, p+1])
		maximumPos = max(dataMat[:, p+1])
		rangeOfPos = float(maximumPos - minimumPos)
		centroids[:, p] = minimumPos + rangeOfPos*(np.random.rand(k, 1))
		print("MinimumPos: ", minimumPos)
		print("MaximumPos: ", maximumPos)
	print(len(centroids), "centroids have been randomly generated.")
	return centroids


def getDistance(vecA, vecB):
	return np.sqrt(np.sum(np.power(vecA - vecB, 2)))
	#return cosine(vecA, vecB)


def kMeans(centroids, dataMat, k):
	num_pts = (np.shape(dataMat)[0])
	clusterAssignment = np.mat((np.zeros((num_pts, 2))))
	clusterChanged = True
	while clusterChanged:
		clusterChanged = False
		for each_point in range(num_pts):
			minDistance = Inf; minIndex = -1 #each_point가 바뀔 때마다 변수를 초기화
			for each_centroid in range(k):
				PtCentDistance = getDistance(centroids[each_centroid, :], dataMat[each_point, 1:]) #each_point와 each_centroid간의 거리 계산1
				if PtCentDistance < minDistance:
					minDistance = PtCentDistance; minIndex = each_centroid
			if clusterAssignment[each_point, 0] != minIndex:
				clusterChanged = True		
			clusterAssignment[each_point, :] = minIndex, each_point

	clusters = []
	for each_centroid in range(k):
		cluster_members = np.nonzero(clusterAssignment[:,0]==each_centroid)[0]
		cluster_matrix = (dataMat[cluster_members][0])

		clusters.append(cluster_members)


		if np.shape(cluster_matrix)[0] != 0:
			centroids[each_centroid, :] = np.mean(cluster_matrix, axis=0)[0, 1:]

	return {"centroids": centroids, "clusters": clusters}