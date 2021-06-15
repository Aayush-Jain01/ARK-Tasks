import cv2 
import numpy as np

image = cv2.imread("/home/aayush/Desktop/ARK_Task-3/Task-3/Level1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
zucky_elon = cv2.imread("/home/aayush/Desktop/ARK_Task-3/Task-3/zucky_elon.png")
# blur = cv2.medianBlur(image, 11)
count = 0
flag = 0
x = 0
for i in range(gray.shape[1]):
    y = 0    
    for j in range(gray.shape[0]):
        print(chr(int(gray[i][j])), end = "")
        image[i][j] = (0, 0, 255)
        count += 1 
        y += 1
        if int(gray[i][j]) == 58:
            image[i][j] = (0, 0, 255)
            flag = 1
            break
    x += 1
    if flag == 1:
        break

print(image.shape)


black_image = np.zeros((200, 150, 3), np.uint8)
countpixel = 0

R = []
G = []
B = []
for i in range(image.shape[1]):
    for j in range(image.shape[0]):    
        if image[i][j][0] == 0 and image[i][j][1] == 0 and image[i][j][2] == 255:
            pass
        else:
            countpixel += 1
            if countpixel > 30000:
                break
            R.append(image[i][j][2])
            G.append(image[i][j][1])
            B.append(image[i][j][0])
    if countpixel > 30000:
        break
i = 0
for x in range(black_image.shape[0]):
    for y in range(black_image.shape[1]):
        black_image[x][y] = (B[i], G[i], R[i])
        i += 1


cv2.imshow("img", black_image)
cv2.waitKey(0)