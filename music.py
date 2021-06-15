import cv2

treasure = cv2.imread('/home/aayush/Desktop/ARK_Task-3/Task-3/treasure_mp3.png')
values = []
gray = cv2.cvtColor(treasure, cv2.COLOR_BGR2GRAY)
for i in range(gray.shape[1]):
    for j in range(gray.shape[0]):
        values.append(gray[i][j])

# for i in range(gray.shape[1]):   
#     for j in range(gray.shape[0]):
        # if int(gray[i][j]) >= 48 and int(gray[i][j]) <= 57:
        #     print(int(gray[i][j]-48), end = "")
        # if int(gray[i][j]) == 58:
        #     print(chr(int(gray[i][j])), end = "")
        # if int(gray[i][j]) >= 65 and int(gray[i][j]) <= 90:
        #     print(chr(int(gray[i][j])), end= "")
        #     image[i][j] = (255, 0, 0)
        # if int(gray[i][j]) >= 97 and int(gray[i][j]) <= 122:
        #     print(chr(int(gray[i][j])), end = "")
        #     image[i][j] = (255, 0, 0)
        # print(chr(int(gray[i][j])), end = "")

print(values)
cv2.imshow("gray", gray)
cv2.waitKey(0)