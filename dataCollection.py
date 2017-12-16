import cv2
import numpy as np
import time

cam = cv2.VideoCapture(1	)

cv2.namedWindow("test")

nH = 164
nV = 108
nS = 13
nN = 82

temp = None

while True:
	ret, frame = cam.read()
	cv2.imshow("test", frame)
	if not ret:
		break
	k = cv2.waitKey(1)

	if k%256 == 27:
		# ESC pressed
		print("Escape hit, closing...")
		break
	elif k%256 == 49:
		# Horizontal pressed
		time.sleep(.1)
		ret, frame1 = cam.read()
		
		frame = np.concatenate((frame, frame1), axis=2)

		np.save('horizontal/horizontal{:>05}'.format(nH), frame)
		
		print("Saved Horizontal: " + str(nH))
		
		nH += 1

	elif k%256 == 50 and temp is None:
		print("Spinning 1/2")
	
		ret, temp = cam.read()
		
	elif k%256 == 50 and temp is not None:
		ret, frame = cam.read()
		
		frame = np.concatenate((temp, frame), axis=2)

		np.save('spinning/spinning{:>05}'.format(nS), frame)
		
		print("Saved Spinning: " + str(nS))
		
		temp = None
		
		nS += 1
	
	elif k%256 == 51:
		# Vertical pressed
		time.sleep(.1)
		ret, frame1 = cam.read()
		
		frame = np.concatenate((frame, frame1), axis=2)

		np.save('vertical/vertical{:>05}'.format(nV), frame)
		
		print("Saved Vertical: " + str(nV))
		
		nV += 1
	
	elif k%256 == 52:
		# Nothing pressed
		time.sleep(.1)
		ret, frame1 = cam.read()
		
		frame = np.concatenate((frame, frame1), axis=2)

		np.save('nothing/nothing{:>05}'.format(nN), frame)
		
		print("Saved Nothing: " + str(nN))
		
		nN += 1


cam.release()

cv2.destroyAllWindows()
