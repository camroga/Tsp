# Local library
from basefile import BaseFile
from tsp import Tsp

import datetime as date
import matplotlib.pyplot as plt
import numpy as np
import sys

class NearestNeighbors(object):
	"""docstring for Tsp"""
	def __init__(self):
		super(NearestNeighbors, self).__init__()
		"""on plane coordinate"""
		plt.ion()

	def buildRoute(self):
		#print date init#
		print "init date: " + str(date.datetime.now())
		coorR = [coor.pop(0)]
		dt = 0
		while coor:
			d, p2 = self.nearestNeighbors(coorR[-1])
			dt += d
			coorR.append(p2)
		dt += Tsp().getDistance(p2, coorR[0])
		coorR.append(coorR[0])
		coorR = np.array(coorR)
		Tsp().drawTsp(coorR[:,0], coorR[:,1], dt)
		#print date end#
		print "end date: " + str(date.datetime.now())
		
	def nearestNeighbors(self, p1):
		d = -1
		pos = -1
		i = 0
		for item in coor[:]:
			dTemp = Tsp().getDistance(p1, item)
			if d == -1 or dTemp < d:
				d = dTemp
				pos = i
			i += 1

		return d, coor.pop(pos)

if __name__ == '__main__':
	nameFile = "data/berlin52.tsp"
	if len(sys.argv) > 1:
		nameFile = "data/" + sys.argv[1]
	coor = BaseFile().getContent(nameFile)
	NearestNeighbors().buildRoute()
	"""off plane coordinate"""
	plt.ioff()
	plt.show()
