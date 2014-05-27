#coding=utf-8
import cv2
import numpy

image = numpy.zeros((320,240,3), numpy.uint8)

filename = 'pic.h'
fileHandle = open(filename)

for a in xrange(0, 320):
	count = 0
	for b in xrange(0, 240):
		t = 1
		while t:
			if fileHandle.read(2) == '0X':
				rgb565 = int(fileHandle.read(2), 16)
				fileHandle.read(1)
				rgb565 = rgb565 | (int(fileHandle.read(4), 16) << 8)
				t = 0
			else:
				fileHandle.seek(fileHandle.tell() - 1)

		R = (rgb565 >> 11) << 3
		G = ((rgb565 >> 5) & 0x3f) << 2
		B = (rgb565 & 0x1f) << 3

		x = count % 240
		y = a % 320

		image[y, x, 0] = R
		image[y, x, 1] = G
		image[y, x, 2] = B

		count = count + 1

fileHandle.close()
cv2.imshow("image", image)

cv2.imwrite("hex2rgb.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
