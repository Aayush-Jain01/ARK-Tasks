import cv2
import numpy as np
img = np.zeros((480,480,3),dtype='uint8')
img2 = np.zeros((480,480,3),dtype='uint8')
dx,dy = 1,2
dx1 = 1
x,y = 0,0
x1,y1 = 0,460
count = 0
flag = 0
while True:
    # Display the images
    f_image = cv2.bitwise_or(img, img2, mask= None)
    cv2.imshow('Collision',f_image)
    # k = cv2.waitKey(10)
    img = np.zeros((480,480,3),dtype='uint8')
    img2 = np.zeros((480,480,3),dtype='uint8') 
    # Increment the position  
    x = x+dx
    y = y+dy
    if flag == 0:
        x1 += dx1
    if flag == 1:
        x1 += 2*dx1
    # y1 += dy
    cv2.circle(img,(x,y),20,(255,0,0),-1)
    cv2.circle(img2,(x1,y1),20,(0,0,255),-1)
    # if k != -1:
    #     break
    # Change the sign of increment on collision with the boundary
    if y >= 480:
        break
    elif y <= 0:
        dy *= -1
    if x >=480:
        dx *= -1
    elif x<=0:
        dx *= -1
    if x1 >= 480 or x1 <= 0:
        dx1 *= -1
    if x1 == x and y == 440:
        dy *= -1
        count += 1
    if count > 6:
        flag = 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()