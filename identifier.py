import cv2 as cv
import pytesseract as pyt

# Reading image
path = "Media files\Images\sample.jpg"
img=cv.imread(path)
iH,iW,_=img.shape
RGB_img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

# Detecting characters
boxes = pyt.image_to_boxes(img)
extra = 2
for b in boxes.splitlines():
    b = b.split()
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv.rectangle(img,(x-extra,iH-y),(w+extra,iH-h),(255,0,255),1)
    cv.putText(img,b[0],(x,iH-y+30),cv.FONT_HERSHEY_SIMPLEX,0.5,(30,200,150),1)
cv.imshow("win",img)
cv.waitKey(0)




