import cv2
import numpy as np

maze = cv2.imread('/home/aayush/Desktop/ARK_Task-3/Task-3/maze_lv3.png')
for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        # if noise[i][j][0] == 230 and noise[i][j][1] == 0 and noise[i][j][2] == 0:
        if maze[i][j][0] == 230:
            pass
        else:
            maze[i][j][0] = 0 
            maze[i][j][1] = 0 
            maze[i][j][2] = 0

# maze[380][23] = (255, 255, 255)
# maze[380][150] = (0, 0, 255)

# img = maze

def rescaleFrame(frame, scale = 0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

image = rescaleFrame(maze)
# image[290][110] = (255, 255, 255)
# image[290][806] = (250, 250, 250)
image[36][13] = (255, 255, 255)
image[36][100] = (250, 250, 250)

print(image.shape)

img = image

class cell:
    def __init__(self, type_, x, y, b, g, r):
        self.type_ = type_
        self.f = 0
        self.g = 0
        self.h = 0
        self.x = x
        self.y = y
        self.b = b
        self.g = g
        self.r = r
        self.previous = None

# def heuristic(pt1, pt2):
#     distance_square = (pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2
#     distance = distance_square**0.5
#     return distance

def heuristic(pt1, pt2):
    distance = abs((pt1.x - pt2.x)) + abs((pt1.y - pt2.y))
    return distance

# def heuristic(pt1, pt2):
#     distance = max(abs((pt1.x - pt2.x)), abs((pt1.y - pt2.y)))
#     return distance

# def heuristic(pt1, pt2):
#     distance_square = (pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2
#     distance = 0.75*(distance_square**0.5)
#     return distance

# def heuristic(pt1, pt2):
#     distance_square = (pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2
#     distance = 2*(distance_square**0.5)
#     return distance

openSet = []
closedSet = []
p4 = []
p3 = []
path = []


# start = [113, 204, 45]
# end = [60, 76, 231]


for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        pixel = img[x, y]
        if (pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255):
            p1 = cell("Start", x, y, pixel[0], pixel[1], pixel[2])
            print(p1.type_)
        if (pixel[0] == 250 and pixel[1] == 250 and pixel[2] == 250):
            p2 = cell("End", x, y, pixel[0], pixel[1], pixel[2])
            print(p2.type_)
        if pixel[0] == 230:
            p3.append(cell("Obstacle", x, y, pixel[0], pixel[1], pixel[2]))
            print("Obstacle")
        if (pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0):
            p5 = cell("Path", x, y, 0, 0, 0)
            p4.append(p5)


              
start = p1
end = p2
allneighbors = p4 + p3
allneighbors.append(end)

openSet.append(start)
count = 0
print("ALGORITHM STARTS")

while(len(openSet) > 0):
    print(len(openSet))
    f_index = 0
    for i in range(len(openSet)):
        if openSet[i].f < openSet[f_index].f:
            f_index = i
    
    current = openSet[f_index] 
    x = current.x
    y = current.y
    
    if current.x == end.x and current.y == end.y:
        print("Target Reached!")
        break
    

    openSet.remove(current)
    closedSet.append(current)    
    
    neighbors = []
   
    for i in range(len(allneighbors)):
        if allneighbors[i].type_ != "Obstacle":
            if allneighbors[i].x == x+1 and allneighbors[i].y == y:
                neighbors.append(allneighbors[i])  

            if allneighbors[i].x == x-1 and allneighbors[i].y == y:
                neighbors.append(allneighbors[i])

            if allneighbors[i].x == x and allneighbors[i].y == y+1:
                neighbors.append(allneighbors[i])

            if allneighbors[i].x == x and allneighbors[i].y == y-1:
                neighbors.append(allneighbors[i])
    
    
    for j in range(len(neighbors)):
        neighbor = neighbors[j]
        closed = False
        for i in range(len(closedSet)):
            if closedSet[i] == neighbor:
                closed = True
        if closed == True:
            continue
        tempg = current.g + 1
        flag = 0
        newPath = False
        for i in range(len(openSet)):
            if openSet[i].x == neighbor.x and openSet[i].y == neighbor.y:
                flag = 1                
                if tempg < neighbor.g:
                    neighbor.g = tempg
                    newPath = True
        if flag != 1:
            newPath = True
            openSet.append(neighbor)
            neighbor.g = tempg

        if(newPath):
            neighbor.h = heuristic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h
            # neighbor.f = neighbor.g
            neighbor.previous = current
    

    for j in range(len(openSet)):
        x = openSet[j].x
        y = openSet[j].y
        if x == end.x and y == end.y:
            continue
        else:
            img[x, y] = (255, 0, 0)
    for j in range(len(closedSet)):
        x = closedSet[j].x
        y = closedSet[j].y
        img[x, y] = (0, 165, 255)    
    count += 1
    # if count > 5000:
    #     break


temp = end.previous
path.append(temp)
    
while(temp.previous):
    path.append(temp.previous)
    temp = temp.previous


for i in range(len(path)):
    x = path[i].x
    y = path[i].y
    img[x, y] = (0, 255, 0)
    count += 1

print("Cost = " + str(count))

def rescaleFrame(frame, scale = 4):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

image_big = rescaleFrame(img)
cv2.imshow("image", image_big)

# cv2.imshow("image", image_big)
# cv2.imshow("original image", image_big)
# cv2.imwrite("Dijkstra Case-1.jpg", image_big)
# cv2.imwrite("Admissible Case-1.jpg", image_big)
# cv2.imwrite("Inadmissible Case-1.jpg", image_big)
# cv2.imwrite("Diagonal Case-1.jpg", image_big)
# cv2.imwrite("Manhatten Case-1.jpg", image_big)
# cv2.imwrite("Euclidean Case-1.jpg", image_big)
cv2.waitKey(0)
