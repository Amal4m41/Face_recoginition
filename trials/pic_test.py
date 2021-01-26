import cv2


pic=cv2.imread('../my_image.png')

#Checking the height,width and depth
# (h, w, d) = pic.shape
# print("width={}, height={}, depth={}".format(w, h, d))

# cv2.imshow("PIC",pic)
# v=cv2.waitKey(0)
# print(v)   #prints the ASCII value of the character.
'''
To display the image on the screen using OpenCV we employ cv2.imshow("Image", image) .
The subsequent line waits for a keypress (Line 11).
This is important otherwise our image would display and disappear faster than we’d even see the image.
'''

#WAITKEY example

# import numpy as np
# import cv2
#
# img = cv2.imread('messi5.jpg',0)
# cv2.imshow('image',img)
# k = cv2.waitKey(0)
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'): # wait for 's' key to save and exit
#     cv2.imwrite('messigray.png',img)
#     cv2.destroyAllWindows()

#Manuall exraction of ROI
# roi=pic[0:120,0:284]  #[y(start):y+h(end),x(start):x+w(end)]  extracting manually the roi.
# cv2.imshow("ROI",roi)
# cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio(i.e resize the whole image)
# resized = cv2.resize(pic, (900, 20))   # w x h
# resized = cv2.resize(pic, (50, 50))   # w x h
# cv2.imshow("Fixed Resizing", resized)
# cv2.waitKey(0)

# roi=pic[0:100,0:200]
# cv2.imshow("ROI",roi)
# cv2.waitKey(0)
# (h,w,d)=roi.shape

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio

pic=cv2.imread('../images/zayn_malik/1.jpg')
(h,w,d)=pic.shape
resize_val=300
r = resize_val / w    #r tells by how much the width is resized compaired to the original width
dim = (resize_val, int(h * r)) #the height is also resized with the same value (therefore aspect ratio is maintained)
print('Resized value : ',resize_val,'x',h*r)
# resized = cv2.resize(pic, dim)
resized = cv2.resize(pic, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)