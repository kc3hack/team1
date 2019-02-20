import tensorflow as tf
import numpy as np
import cv2
import os

def predict(image):
    graph_def = tf.GraphDef()

    with tf.gfile.FastGFile("model.pb", 'rb') as f:
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        prob_tensor = sess.graph.get_tensor_by_name('loss:0')
        predictions, = sess.run(prob_tensor, {'Placeholder:0': [x] })
        return np.argmax(predictions)