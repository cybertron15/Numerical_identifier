import cv2 as cv
import pytesseract as pyt

class identifier():
    def __init__(self,path):
        """initializes all the required variables"""
        # Reading image
        path = path
        self.img = cv.imread(path)

        # Getting original image Dimentions
        self.height, self.width, _ = self.img.shape

        # Coverting to RGB because pytesseract works better with RGB images and OpenCV by default has BGR
        self.RGB_img = cv.cvtColor(self.img,cv.COLOR_BGR2RGB)
    
    
    def get_numbers(self):
        """gets all the numbers present on the image"""

        confg = r"--oem 3 --psm 6 outputbase digits" #this setting is basiclly setting the enginemode(oem) and psm(page segmentation) this values are passed refering to doucmentation
        # Getting the string of character and the bounding bixed info
        boxes = pyt.image_to_data(self.RGB_img,config=confg)
        
        string = ""
        for i,line in enumerate(boxes.splitlines()):
            if i>0: # setting this to skip the first line cosisting of labels
                item = line.split() 
                if len(item) == 12: # checking for the lines with words as it has legth of 12
                    x,y,w,h = int(item[6]),int(item[7]),int(item[8]),int(item[9])
                    cv.rectangle(self.img,(x,y),(x+w,y+h),(0,0,255),1)# drawing bounding boxed
                    cv.putText(self.img,item[11],(x,y+40),cv.FONT_HERSHEY_PLAIN,1.3,(255,0,0),1) # writing character below the box
                    string += item[11] + " "
                    print(string)
        
        return self.img

    
    def get_data(self):
        """gets all the data present on the image"""

        # Getting the string of character and the bounding bixed info
        boxes = pyt.image_to_data(self.RGB_img)
        
        string = ""
        for i,line in enumerate(boxes.splitlines()):
            if i>0: # setting this to skip the first line cosisting of labels
                item = line.split() 
                if len(item) == 12: # checking for the lines with words as it has legth of 12
                    x,y,w,h = int(item[6]),int(item[7]),int(item[8]),int(item[9])
                    cv.rectangle(self.img,(x,y),(x+w,y+h),(0,0,255),1)# drawing bounding boxed
                    cv.putText(self.img,item[11],(x,y+40),cv.FONT_HERSHEY_PLAIN,1.3,(255,0,0),1) # writing character below the box
                    string += item[11] + " "
        print(string)
        
        return self.img

    
    def get_characters(self):
        """gets indivisual characters from the image"""

        boxes = pyt.image_to_boxes(self.RGB_img)
        # Converting each line of the string into list for better accesibility
        # string = ""
        for line in boxes.splitlines():
            item = line.split()
            print(item)
            x,y,w,h = int(item[1]),int(item[2]),int(item[3]),int(item[4])

            #here hight and y is given inverted so we need to subtract it from the immage height
            cv.rectangle(self.img,(x,self.height-y),(w,self.height-h),(0,0,255),1)# drawing bounding boxed
            cv.putText(self.img,item[0],(x,self.height-y+20),cv.FONT_HERSHEY_PLAIN,1,(255,0,0),1) # writing character below the box
        
        return self.img 

    
    def get_string(self):
        """returnsstrig present inside an image"""

        string = pyt.image_to_string(self.RGB_img) 
        return string


    def show(self,img):
        """Shows the image"""

        cv.imshow('w',img)
        cv.waitKey(0)


identify = identifier(r"Media files\Images\sample.jpg")
img = identify.get_data()
identify.show(img)


