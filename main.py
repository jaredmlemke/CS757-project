#!/usr/bin/env python

import sys
import numpy
import os

try:
    import numpy
except:
    print "This implementation requires the numpy module."
    exit(0)

def main():
	#os.system("hadoop fs -mkdir proj/input");	
	#os.system("hadoop fs -mkdir proj/output");
	#os.system("hadoop fs -put V.arr proj/input");

	# Data dimensions 49
	rdim = 19
	# len(V) The number of rows in V - For Faces dataset it is 361
	# This is the number of users
	vdim = 943 
	# len(input[0]) The number of columns in V - For Faces dataset it is 2429
	samples = 1682 
	
	# 943 x 1682 = 1586126	

	# Create initial matrices: 
	# vdim-by-rdim matrix of normally distributed random numbers.
	W = abs(numpy.random.rand(vdim,rdim))
	# rdim-by-samples matrix of normally distributed random numbers.
	H = abs(numpy.random.rand(rdim,samples))

	# Save W and H to a file
	numpy.savetxt('w.arr', W, '%.18e', delimiter=' ')
	numpy.savetxt('h.arr', H, '%.18e', delimiter=' ')
	
	# Initial stepsizes
	stepsizeW = 1;
	stepsizeH = 1;

	# Start iteration
	iter = 0;

	while True:
		# ***** This is for H *****
		isForH = True;

		# Gradient for H
		# Map/Reduce Job 1
                # ####  Maper: send one V row to the reducer
		# ####  Reducer: calculate the gradient dH = W'*(W*H-V);
		#os.system("hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar  -input proj/input/V.arr -output proj/output/ -mapper mapper-1.py -reducer reducer-1.py  -file mapper-1.py -file reducer-1.py")
		
		if True: # When to break
			break

if __name__ == "__main__":
    main()
