# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 14:47:09 2023

@author: Admin
"""

import cv2

def capture_image(frame, counter):
    filename = f"captured_image_{counter}.png"
    cv2.imwrite(filename, frame)
    print("Image captured successfully as", filename)

video = cv2.VideoCapture(1)
counter = 0

while True:
    ret, frame = video.read()
    cv2.imshow('Webcam', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):  
        capture_image(frame, counter)
        counter += 1

video.release()
cv2.destroyAllWindows()
