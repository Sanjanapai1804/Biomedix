import numpy as np
import cv2
import glob
import argparse

# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='Stereo Calibration')
    parser.add_argument('--imagesL', required=True, help='E:\write\images2')
    parser.add_argument('--imagesR', required=True, help='E:\write\images3')
    return parser.parse_args()

# termination criteria for the iterative algorithm
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpointsL = []  # 2d points in image plane.
imgpointsR = []  # 2d points in image plane.

# Parse command-line arguments
# Parse command-line arguments
args = parse_arguments()
imagesL = glob.glob(args.imagesL + '/*.png')
imagesR = glob.glob(args.imagesR + '/*.png')

for fnameL, fnameR in zip(imagesL, imagesR):
    imgL = cv2.imread(fnameL)
    imgR = cv2.imread(fnameR)
    grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    retL, cornersL = cv2.findChessboardCorners(grayL, (7, 6), None)
    retR, cornersR = cv2.findChessboardCorners(grayR, (7, 6), None)

    # If found, add object points, image points (after refining them)
    if retL == True and retR == True:
        objpoints.append(objp)

        corners2L = cv2.cornerSubPix(grayL, cornersL, (11, 11), (-1, -1), criteria)
        imgpointsL.append(corners2L)

        corners2R = cv2.cornerSubPix(grayR, cornersR, (11, 11), (-1, -1), criteria)
        imgpointsR.append(corners2R)

# Assuming you have some images in imagesL, take the first one just to get the shape
first_image_path = imagesL[0]
first_image = cv2.imread(first_image_path)
height, width = first_image.shape[:2]

# Initializations with default values
mtxL = mtxR = np.array([[1, 0, width / 2], [0, 1, height / 2], [0, 0, 1]], dtype=float)
distL = distR = np.zeros((5, 1), dtype=float)

# Perform stereo calibration
ret, mtxL, distL, mtxR, distR, R, T, E, F = cv2.stereoCalibrate(
    objectPoints=objpoints,
    imagePoints1=imgpointsL,
    imagePoints2=imgpointsR,
    cameraMatrix1=mtxL,
    cameraMatrix2=mtxR,
    distCoeffs1=distL,
    distCoeffs2=distR,
    imageSize=(width, height),
    flags=cv2.CALIB_FIX_INTRINSIC
)

print('Intrinsic_mtx_1:', mtxL)
print('dist_1:', distL)
print('Intrinsic_mtx_2:', mtxR)
print('dist_2:', distR)
print('R:', R)
print('T:', T)
print('E:', E)
print('F:', F)

