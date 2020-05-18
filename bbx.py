from absl import logging
import numpy as np
import tensorflow as tf
import cv2

def get_vertices(img, boxes, nums):
    boxes = boxes[0]
    nums = nums[0]
    for i in range(nums):
        wh = np.flip(img.shape[0:2])
        x1y1 = tuple((np.array(boxes[i][0:2]) * wh).astype(np.int32))
        x2y2 = tuple((np.array(boxes[i][2:4]) * wh).astype(np.int32))
    
    return x1y1, x2y2
    