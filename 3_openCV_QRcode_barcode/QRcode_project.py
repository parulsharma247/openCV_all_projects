#########################  Read QR code from Image ##############################
# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode # decode gives info about QR code and its coordinates also
#
# path = r"C:\Users\om\PycharmProjects\openCV_projects\Images\QRcode_Images\1.png"
# img = cv2.imread(path)
#
#
# # print(decode(img))
# '''
# print(decode(img)) -> Its o/p is mentioned below:
# [Decoded(data=b'111111', type='QRCODE', rect=Rect(left=84, top=176, width=76, height=75),
# polygon=[Point(x=84, y=176), Point(x=84, y=251), Point(x=160, y=251), Point(x=159, y=176)])]
#
# "data" -> is the data inside barcode/QRcode
# "rect" -> bounding box coordinates
# "polygon" -> QR code is not completely rectangle so polygon gives us various coordinates
# '''
#
# for barcode in decode(img):
#     print(f'data in QR code = {barcode.data}')  # to print the information inside QRcode but that info is in bytes
#     print(f"boundingg box coordinates = {barcode.rect}\nPolygon coordinates = {barcode.polygon}")
#     mydata = barcode.data.decode('utf-8') # changed the data from byte to string
#     print(mydata)


#################################  For QR bar Test  ###########################################

'''import cv2
import numpy as np
from pyzbar.pyzbar import decode  # to decode QRcode and barcode

# img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')  # changed the data from byte to string
        # print(myData)
        pts = np.array([barcode.polygon], np.int32)  # getting polygon coordinates in an array
        print(f'pts w/o reshape = {pts}')

        # pts = pts.reshape((-1, 1, 2))
        # print(f'pts with reshape = {pts}')

        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect  # getting the rectangle coordinates
        print(f'pts2 = {pts2}')  # here we use these points to put the text always from the top-left side
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 255), 2)  #

    cv2.imshow('Result', img)
    cv2.waitKey(1)  # wait for 1 milli-second'''

######################  for QRcode Test  #################################

import cv2
import numpy as np
from pyzbar.pyzbar import decode

# path = r"C:\Users\om\PycharmProjects\openCV_projects\Images\QRcode_Images\Qr (1).png"
# img = cv2.imread(path)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# myDataFile is like a database where we have stored the info regarding QRcodes
with open('myDataFile.txt') as f:
    myDataList = f.read().splitlines()
    print(myDataList)

while True:

    success, frame = cap.read()
    for barcode in decode(frame):
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0, 255, 0)
        else:
            myOutput = 'Un-Authorized'
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, myColor, 5)
        pts2 = barcode.rect
        cv2.putText(frame, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, myColor, 2)

    cv2.imshow('Result', frame)
    cv2.waitKey(1)

