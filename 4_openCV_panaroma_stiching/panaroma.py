import cv2
import os

mainFolder = 'Images_panaroma'
myFolders = os.listdir(mainFolder)  # gives list of directories inside 'Images_panaroma'
print(myFolders)

for folder in myFolders: # folder is 1, then 2,.... and so on for further folders
    path = mainFolder + '/' + folder
    images = []
    myList = os.listdir(path)
    print(f'Total no of images detected {len(myList)}')
    for imgN in myList:
        curImg = cv2.imread(f'{path}/{imgN}')
        # we will not reduce by pixels (0,0), we will only reduce the scale
        curImg = cv2.resize(curImg, (0, 0), None, 0.2, 0.2)
        images.append(curImg)

    stitcher = cv2.Stitcher.create()  # creating an stitcher object
    (status, result) = stitcher.stitch(images) # stich all the images together
    print('status = ', status)
    if status == cv2.STITCHER_OK:
        print('Panorama Generated')
        cv2.imshow(folder, result)
        cv2.waitKey(1)
    else:
        print('Panorama Generation Unsuccessful')

cv2.waitKey(0)
