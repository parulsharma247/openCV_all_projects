import cv2
import numpy as np

path = r"\Users\om\PycharmProjects\openCV_projects\Images\man_neural_network.jpg"
img = cv2.imread(path)
print(img.shape)

imgResize = cv2.resize(img,(800,500))

cv2.imshow("Output", img)
cv2.imshow("Output resize", imgResize)
cv2.waitKey(0)
