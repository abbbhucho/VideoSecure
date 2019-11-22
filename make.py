import cv2
import numpy as np
import os, shutil
 
from os.path import isfile, join

def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    try:
        files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, 'images_hidden.bmp'))]
        #print(files[2])
        filename=pathIn + files[2]
    except IndexError:
        files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
        #print(files[0])
        filename=pathIn + files[0]    

    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    frame_array.append(img)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    out.write(frame_array[0])
    out.release()
