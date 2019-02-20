import cv2
import numpy as np
import glob

def execute():
    takoyaki_list = glob.glob( "takoyaki/*.jpeg" )
    okonomiyaki_list = glob.glob( "okonomiyaki/*jpg" )
    size = ( 242, 242 )
    x_data = np.zeros(( 1, 3, 242, 242 ))
    x_data_instance = np.zeros(( 1, 3, 242, 242 ))
    answer_data = np.array( [] )
    
    for i in range( 0, len( takoyaki_list ) ):
        img = cv2.imread( takoyaki_list[i],  cv2.IMREAD_COLOR )
        new_img = cv2.resize( img, size )
        new_img = new_img.transpose()
        x_data_instance[0] = np.copy( new_img ) 
        np.append( answer_data, int( 0 ) )
        if i == 0:
            x_data[0] = np.copy( x_data )
        else:
            x_data = np.vstack(( x_data, x_data_instance ))

    for i in range( 1, len( okonomiyaki_list ) ):
        img = cv2.imread( okonomiyaki_list[i],  cv2.IMREAD_COLOR )
        new_img = cv2.resize( img, size )
        new_img = new_img.transpose()
        x_data_instance[0] = np.copy( new_img )
        np.append( answer_data, int( 1 ) )
        x_data = np.vstack( ( x_data, x_data_instance ) )

    x_data = x_data.astype( np.float32 )
    return x_data, answer_data
    
