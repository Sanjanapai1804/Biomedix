# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 12:41:23 2023

@author: Admin
"""

import cv2

def capture_image(frame):
    
    filename = "captured_image.jpg"
    cv2.imwrite(filename, frame)
    print("Image captured successfully as", filename)

video = cv2.VideoCapture(1)

while True:
    ret, frame = video.read()
    cv2.imshow('Webcam', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):  # Press 'q' to quit
        break
    elif key == ord('c'):  # Press 'c' to capture image
        capture_image(frame)

video.release()
cv2.destroyAllWindows()


        