import cv2
import numpy as np

picname = "rgb2hex.jpg"
image = cv2.imread(picname)

image_width = image.shape[0]
image_height = image.shape[1]

hexname = 'pic.h'
fileHandle = open(hexname, 'w')

for x in xrange(0,320):
	for y in xrange(0,240):
		R = image[x,y,0]
		G = image[x,y,1]
		B = image[x,y,2]

		RGB565 = ((R >> 3) << 11) | ((G >> 2) << 5) | (B >> 3)
		RGB565_H = (RGB565 & 0xff00) >> 8
		RGB565_L = RGB565 & 0x00ff
		fileHandle.write('0X%02X,' % RGB565_L)
		fileHandle.write('0X%02X,' % RGB565_H)
		if (y + 1) % 8 == 0:
			fileHandle.write('\n')

cv2.waitKey(0)
cv2.destroyAllWindows()
