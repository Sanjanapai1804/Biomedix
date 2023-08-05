# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:30:45 2023

@author: Admin
"""

import cv2
import os

def capture_image(frame, counter, camera, folder):
    filename = f"captured_image_{counter}.png"
    save_path = os.path.join(folder, filename)
    cv2.imwrite(save_path, frame)
    print("Image captured successfully as", save_path)

camera_index1 = 1
camera_index2 = 2

output_folder1 = "camera1_images"
output_folder2 = "camera2_images"

if not os.path.exists(output_folder1):
    os.makedirs(output_folder1)
if not os.path.exists(output_folder2):
    os.makedirs(output_folder2)

video1 = cv2.VideoCapture(camera_index1)
video2 = cv2.VideoCapture(camera_index2)
counter = 0

while True:
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()

    cv2.imshow('Webcam 1', frame1)
    cv2.imshow('Webcam 2', frame2)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        capture_image(frame1, counter, camera_index1, output_folder1)
        capture_image(frame2, counter, camera_index2, output_folder2)
        counter += 1

video1.release()
video2.release()
cv2.destroyAllWindows()

