from chainer.links import ResNet152Layers
import numpy as np
from sklearn import datasets
import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import learn_data

def learn(image_x = [], image_y = [], vec = [], test_num = 5):
    model = ResNet152Layers()

    for x in image_x[:-test_num] + image_y[:-test_num]:
        vec.append(model(np.zeros((3,3,224,224), dtype=np.float32))["prob"])

    vec = np.array(vec)
    y_train = np.hstack([np.zeros(len(image_x)-test_num), np.ones(len(image_y)-test_num)])

    svm = SVC(kernel='linear', random_state=None)
    svm.fit(vec, y_train)

    acc = accuracy_score(y_train, svm.predict(vec))
    print('acc： %d%%' % acc*100)

def main():
    x, y = learn_data.execute()
    print(x)
    print(y)

if __name__ == '__main__':
    main()