import cv2
img_file = 'Enter Image Here'
classifier_file = 'car_detector.xml'
img = cv2.imread(img_file)
black_and_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
car_tracker = cv2.CascadeClassifier(classifier_file)
cars = car_tracker.detectMultiScale(black_and_white)
for (x, y, w, h) in cars:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)
cv2.imshow('Car_Detection',img)
cv2.waitKey()
print("Code Completed")
