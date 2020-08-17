import cv2
import pytesseract

# importing the terreract library
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

image_path = r"\Users\om\PycharmProjects\openCV_projects\Images\text_detection.png"
image = cv2.imread(image_path)  # reading the image

def word_detection(img):
    hImg, wImg,_ = img.shape # getting the height and width of image
    # print(f'hImg={hImg}, wImg={wImg}')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting the image to RGB as pytesseract reads RGB only

    boxes = pytesseract.image_to_data(img)
    # print('boxes =\n',boxes,'\n......boxes end here......')

    for a, b in enumerate(boxes.splitlines()):
        print(a)
        print(b)
        if a != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.putText(img, b[11], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
                cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 255), 2)

    cv2.imshow('img', img)
    cv2.waitKey(0)

word_detection(image)