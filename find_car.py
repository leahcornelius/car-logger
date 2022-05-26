import cv2

cap = cv2.VideoCapture('cars.avi')
car_detector = cv2.CascadeClassifier('car.xml')
 
while True:
    # Get the seperate frames
    ret, frames = cap.read()
     
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
   
    # Detects each car
    cars = car_detector.detectMultiScale(gray, 1.1, 1)
     
    # To draw a rectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
 
   # Display frames in a window 
   cv2.imshow('video2', frames)
     
    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break
 
# De-allocate any associated memory usage
cv2.destroyAllWindows()
