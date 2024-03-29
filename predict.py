import tensorflow as tf
import numpy as np
import cv2
import os

def execute( img ):
    size = ( 224, 224 )
    new_img = cv2.resize( img, size )
    check = predict( new_img )
    if check == 0:
        return "お好み焼き"
    elif check == 1:
        return "たこ焼き"
    return "わからない"
    
def predict(image):

    graph_def = tf.GraphDef()

    with tf.gfile.FastGFile("model.pb", 'rb') as f:
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        prob_tensor = sess.graph.get_tensor_by_name('loss:0')
        predictions, = sess.run(prob_tensor, {'Placeholder:0': [image] })
        return np.argmax(predictions)

#im = cv2.imread( "okonomiyaki/001.jpg" )
#print(execute(im))

