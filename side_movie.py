#!/usr/bin/python

import numpy as np
import cv2

cap = cv2.VideoCapture("/home/ams/Projects/techomagic_death_curse/Donald Trump's full economic speech-H_EGeoUdTnA.mp4")

if cap.isOpened():
	#Get the height and width of the frame for future use
	ret, frame = cap.read()
	height, width = frame.shape[:2]

	#Set up a numpy array to hold frames and get enough frames to fill it
	frames = []

	for frameCount in range(height):
		frames.append(frame)
		ret, frame = cap.read()
	
	# Release the capture
	cap.release()
	#Convert it to a numpy array... 
	videoBlock = np.array(frames)

	#Now start generating frames by slicing off the, uh, top of the array
	#This is essentially viewing the data as a rectangular prism of data, with
	#an X, Y, and Time axis, and then swapping the X and Time axes. 
	#Trust me. 
	fourcc = cv2.cv.CV_FOURCC(*'XVID')
	out = cv2.VideoWriter("out.avi", fourcc, 20.0, (width, height))
	for frameCount in range(height):
		newFrame = videoBlock[:,frameCount,:,:]
		out.write(newFrame)
		cv2.imshow('frame', newFrame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	out.release()
