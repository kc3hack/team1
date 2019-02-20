from chainer.links import ResNet101Layers
import numpy as np
from sklearn import datasets
import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import learn_data
import chainer.computational_graph as c

def make_vec(image_x = [], image_y = [], test_num = 10):
    model = ResNet101Layers()

    vec_0 = []
    vec_1 = []
    for x in image_x:
        vec_0.append(model(x.reshape(1, *x.shape))["prob"].data[0])
    for x in image_y:
        vec_1.append(model(x.reshape(1, *x.shape))["prob"].data[0])
        
    x_train = vec_0[:-test_num]+vec_1[:-test_num]
    y_train = np.hstack([np.zeros(len(image_x)-test_num), np.ones(len(image_y)-test_num)])
    x_test = vec_0[-test_num:]+vec_1[-test_num:]
    y_test = np.hstack([np.zeros(test_num), np.ones(test_num)])

    return x_train, y_train, x_test, y_test

def learn(x_train, y_train, x_test, y_test, kernel='rbf'):
    svm = SVC(kernel=kernel, random_state=None)
    svm.fit(x_train, y_train)
    print(svm.predict(x_test))
    print(y_test)
    print(svm.predict(x_train))
    print(np.sum(y_train==0))
    train_acc = accuracy_score(y_train, svm.predict(x_train))
    test_acc = accuracy_score(y_test, svm.predict(x_test))
    print('train acc： %.1f%%' % (train_acc*100))
    print('test acc ： %.1f%%' % (test_acc*100))

def main():
    x_0, x_1 = learn_data.execute()
    print(len(x_0))
    print(len(x_1))
    hoge = make_vec(x_0, x_1)
    np.savez("vector.npz", *hoge)
    # fuga = np.load("vector.npz")
    # hoge = [fuga[x] for x in fuga.files]
    # for x in hoge:
    #     print(x.shape)
    #     print(np.linalg.norm(x))
    learn(*hoge)


if __name__ == '__main__':
    main()