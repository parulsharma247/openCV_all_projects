import cv2
import math
import os

# print(os.getcwd())

path = r'C:\Users\om\PycharmProjects\openCV_projects'
img_path = os.path.join(path,'Images\\angle_detection2.png')
img = cv2.imread(img_path)

pointsList = []

# make sure 1st click will be on the common point where we want to find the angle

def mousePoints(event, x, y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:  # capture the left click of mouse
        print(x, y)  # whenever we do left click, it will print x, y coordinates of that point
        size = len(pointsList)
        if size != 0 and size % 3 != 0:  # check whether size is not equal to ZERO and not divisible by 3
            cv2.line(img, tuple(pointsList[round((size - 1) / 3)*3]), (x, y), (0, 0, 255), 2)
            # tuple is multiplied by 3 to get the 1st point after every 3 points
            #print(f'pt1 = {tuple(pointsList[round((size - 1) / 3)*3])} pt2 = ({x},{y})')
        cv2.circle(img, (x, y), 3, (0, 0, 255), cv2.FILLED)  # to draw a circle where we have a click
        pointsList.append([x, y])  # appends all clicks to 'pointsList'


def gradient(pt1, pt2):  # finding the slope of line i.e m = (y' -y)/(x'-x)
    return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])


def getAngle(pointsList):  # to find the angle
    pt1, pt2, pt3 = pointsList[-3:]  # to get the last 3 points
    m1 = gradient(pt1, pt2)
    m2 = gradient(pt1, pt3)
    angR = math.atan((m2 - m1) / (1 + (m2 * m1))) # angle = tan_inverse[(m1 - m2)/(1 + m1m2)] and its in Radian
    angD = round(math.degrees(angR)) # changing angle to degree
    if angD < 0:
        angD = angD*(-1)
        cv2.putText(img, str(angD), (pt1[0] - 20, pt1[1] - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)

    else:
        cv2.putText(img, str(angD), (pt1[0] - 20, pt1[1] - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)

    return print(angD)


while True:

    if len(pointsList) % 3 == 0 and len(pointsList) != 0: # run when we have 3 or multiple of 3 points
        getAngle(pointsList)

    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mousePoints) # for any mouse event on 'Image' it will call function mousePoints
    if cv2.waitKey(1) & 0xFF == ord('q'):  # if any wrong click is pressed
        pointsList = []  # empty the pointList i.e type of refresh the list
        img = cv2.imread(path)
