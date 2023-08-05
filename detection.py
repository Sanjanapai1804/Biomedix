# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:05:52 2023

@author: Admin
"""

import cv2

for i in range(10):
    video = cv2.VideoCapture(i)
    if video.isOpened():
        print(f"Camera index {i} is available")
        video.release()
