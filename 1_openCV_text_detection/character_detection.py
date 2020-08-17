import cv2
import pytesseract

# importing the terreract library
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

image_path = r"\Users\om\PycharmProjects\openCV_projects\Images\text_detection.png"
image = cv2.imread(image_path)  # reading the image


def character_detection(img):
    hImg, wImg, _ = img.shape  # getting the height and width of image
    # print(f'hImg={hImg}, wImg={wImg}')

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting the image to RGB as pytesseract reads RGB only
    boxes = pytesseract.image_to_boxes(img) # returns character and its coordinates
    # print('boxes =',boxes,'\n......boxes end here......')

    for b in boxes.splitlines():
        #print(b)
        b = b.split(' ')
        # print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
        # print(f'y={hImg-y}, h= {hImg-h}')
        cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)

    cv2.imshow('img', img)
    cv2.waitKey(0)

character_detection(image) # calling the function
