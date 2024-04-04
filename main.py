import cv2
import numpy as np

#colored image
img=cv2.imread("happy.jpg",cv2.IMREAD_COLOR)

#grayscale image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Blur image using 3x3 kernel
gray_blurred=cv2.blur(gray,(3,3))

#Apply Hough transformation on blurred image.
detected_circles=cv2.HoughCircles(gray_blurred,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=1,maxRadius=40)

#Draw Circle
if detected_circles is not None:
    # Convert the circle parameters a, b and r to integers.
    #The value of a (x-coordinate of the center), b (y-coordinate of the center)
    detected_circles=np.uint16(np.around(detected_circles)) #output:[a,b,r] where : represents all indexes
    for i in detected_circles[0,:]:
        a,b,r=i[0],i[1],i[2]
        #draw circumference
        cv2.circle(img,(a,b),r,(0,255,0),2)
        #draw centers
        cv2.circle(img,(a,b),1,(0,0,255),3)
    cv2.imshow("Circle Detection",img)
    cv2.waitKey(0)
cv2.destroyAllWindows()

