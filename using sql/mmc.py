import cv2


cv2.VideoCapture(akiyo_cif.yuv)
i=cv2.VideoCapture.open(akiyo_cif.yuv)
if cv2.VideoCapture.isOpened(i):
	print "hello"
else:
	print "error" 