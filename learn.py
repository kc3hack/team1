from chainer.links import ResNet152Layers
import numpy as np
from sklearn import datasets
import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import learn_data

def make_vec(image_x = [], image_y = [], test_num = 5):
    model = ResNet152Layers()

    vec_0 = []
    vec_1 = []
    for x in image_x:
        vec_0.append(model(np.zeros((3,3,224,224), dtype=np.float32))["prob"])
    for x in image_y:
        vec_1.append(model(np.zeros((3,3,224,224), dtype=np.float32))["prob"])
        
    x_train = vec_0[:-test_num]+vec_1[:-test_num]
    y_train = np.hstack([np.zeros(len(image_x)-test_num), np.ones(len(image_y)-test_num)])
    x_test = vec_0[-test_num:]+vec_1[-test_num:]
    y_test = np.hstack([np.zeros(test_num), np.ones(test_num)])

    return x_train, y_train, x_test, y_test

def learn(x_train, y_train, x_test, y_test, kernel='linear'):
    svm = SVC(kernel=kernel, random_state=None)
    svm.fit(x_train, y_train)

    acc = accuracy_score(y_test, svm.predict(x_test))
    print('acc： %d%%' % acc*100)

def main():
    x_0, x_1 = learn_data.execute()
    hoge = make_vec(x_0, x_1)
    np.savez("vector.npz", *hoge)
    learn(*hoge)


if __name__ == '__main__':
    main()