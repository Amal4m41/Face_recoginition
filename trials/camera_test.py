import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    some = cv2.cvtColor(frame, cv2.COLOR_BGR2Luv)

    cv2.imshow('frame1',frame)
    cv2.imshow('frame2_gray',gray)
    cv2.imshow('frame3',some)
    cv2.imshow('frame4',frame)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()