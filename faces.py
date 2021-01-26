import cv2,pickle

face_cascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')  # Reading the stored trained model.


with open("label_ids.pickle",'rb') as fr:    #Loading the label-id relation to get the name of the labels.
    og_labels=pickle.load(fr)

#labels are of the form {name:id} we want to invert this forma to {id:name}
labels={k:v for v,k in og_labels.items()}


print(labels)
# face_cascade=cv2.CascadeClassifier('haarcascade_profileface.xml')

cap=cv2.VideoCapture(0)
count=c=0
while True:
    count+=1
    ret,frame = cap.read()
    # print(ret,frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5)

    # print("FACES : ",faces)
    # print(type(frame))   #The frames are automatically converted into numpy arrays of pixels.
    for (x,y,w,h) in faces:
    # if(faces):
    #     (x,y,w,h)=faces

        c+=1
        # print(x,y,w,h)
        roi_gray=gray[y:y+h,x:x+w]  #roi(region of interest)
        # roi_color=frame[y:y+h,x:x+w]
        id,confidence=recognizer.predict(roi_gray)
        print(id,confidence)
        if(confidence>70):
            print("PREDICTED : ",labels[id])
            font=cv2.FONT_HERSHEY_SIMPLEX
            name=labels[id]
            clr=(255,255,255);thickness=2
            cv2.putText(frame,name,(x,y),font,1,clr,thickness,cv2.LINE_AA)

        #To save the image
        # img_name='my_image.png'
        # cv2.imwrite(img_name,roi_gray)
        # cv2.imwrite("new_image.png",roi_color)

        color=(255,0,0) #BGR 0-255
        thickness=2
        end_coord_x=x+w
        end_coord_y=y+h
        cv2.rectangle(frame,(x,y),(end_coord_x,end_coord_y),color,thickness)  #Drawing the rectangle on the frame

    cv2.imshow('frame1',frame)

    k=cv2.waitKey(20)     #the key is recieved and converted into ascii value
    # if cv2.waitKey(20) & 0xFF==ord('q'):    the ascii value is the multiplied with 0xFF which is 255 in hexadecimal(i.e BITWISE and operation and check the value to ord('q'))
    if k==113:  #compairing with the ordinal/ascii value of 'q'
        break

print("No. of frames : ",count,"No. of times face detected : ",c)
cap.release()
cv2.destroyAllWindows()