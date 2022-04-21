import cv2

def takePicture():
    capture = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = capture.read()
        cv2.imwrite("pic.jpg",frame)
        result = False
    
    capture.release()
    cv2.destroyAllWindows()

takePicture()