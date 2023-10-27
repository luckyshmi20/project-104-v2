import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,300), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))
cv2.putText(img,"Mercury",(130,240), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))
cv2.putText(img,"Venus",(200,240), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))
cv2.putText(img,"Earth",(290,240), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))
cv2.putText(img,"Mars",(390,240), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))
cv2.putText(img,"Jupiter",(550,240), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))
cv2.putText(img,"Saturn",(780,240), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))
cv2.putText(img,"Uranus",(980,240), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))
cv2.putText(img,"Neptune",(1110,240), fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))

cv2.imshow("display image", img)
cv2.waitKey(0)