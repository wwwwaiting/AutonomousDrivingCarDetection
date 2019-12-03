import numpy as np
import scipy as sp
import cv2
from matplotlib import pyplot as plt
from disparity import *
from skimage import io
from disparity import *
from depth import *

def compute_3d(depth, px, py, f):
    [M, N] = depth.shape
    image_3d = np.zeros((M,N,3))

    x_2d = np.zeros((M,N))
    y_2d = np.zeros((M,N))

    x_3d = (x_2d - px) * depth / f
    y_3d = (y_2d - py) * depth / f

    image_3d[:,:,0] = x_3d
    image_3d[:,:,1] = y_3d
    image_3d[:,:,2] = depth

    return image_3d

if __name__ == "__main__":
    im_left_path = "train/image_left/um_000000.jpg"
    im_right_path = "train/image_right/um_000000.jpg"
    # read images
    # im_left = io.imread(im_left_path)
    im_left = cv2.imread(im_left_path)
    im_left = cv2.cvtColor(im_left, cv2.COLOR_BGR2RGB)
    # im_right = io.imread(im_right_path)
    im_right = cv2.imread(im_right_path)
    im_right = cv2.cvtColor(im_right, cv2.COLOR_BGR2RGB)

    # compute disparity map
    disparity = compute_disparity(im_left, im_right)

    calib_file_dir = 'train/calib/um_000000.txt'
    f,T,px,py,depth = compute_depth(calib_file_dir, disparity)

    location_3d = compute_3d(depth, px, py, f)
    print(location_3d)