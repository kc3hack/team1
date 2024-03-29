import cv2
import numpy as np
import glob

def execute():
    takoyaki_list = glob.glob( "takoyaki/*.jpeg" )
    # print(len( takoyaki_list ) )
    # print(takoyaki_list )
    okonomiyaki_list = glob.glob( "okonomiyaki/*jpg" )
    # print(len( okonomiyaki_list ) )
    # print(okonomiyaki_list )
    size = ( 224, 224 )
    
    x_0 = []
    for i in range(len( takoyaki_list ) ):
        img = cv2.imread( takoyaki_list[i],  cv2.IMREAD_COLOR )
        new_img = cv2.resize( img, size )
        new_img = new_img.transpose()
        x_0.append(new_img)
    x_0 = np.array(x_0, dtype=np.float32)

    x_1 = []
    for i in range(len( okonomiyaki_list ) ):
        img = cv2.imread( okonomiyaki_list[i],  cv2.IMREAD_COLOR )
        new_img = cv2.resize( img, size )
        new_img = new_img.transpose()
        x_1.append(new_img)
    x_1 = np.array(x_1, dtype=np.float32)

    return x_0, x_1
