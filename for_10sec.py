import cv2
import time

cap = cv2.VideoCapture(1)
while True:

  for i in range(10):
    ret, frame = cap.read()
    time.sleep(10)
    cv2.imwrite(f'data/sample_{i}.jpg', frame)

  break   

cap.release()
cv2.destroyAllWindows()