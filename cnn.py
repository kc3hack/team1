import numpy as np
from chainer import serializers
import chainer
from chainer import cuda, Function, gradient_check, Variable, optimizers, serializers, utils
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L

import learn_data


class CNN(Chain):
    def __init__(self):
        super(CNN, self).__init__(
            conv0 = L.Convolution2D(3, 6, 3, pad = 1),
            conv1 = L.Convolution2D(6, 10, 3, pad = 1),
            conv2 = L.Convolution2D(10, 10, 3, pad = 1),
            conv3 = L.Convolution2D(10, 5, 3, pad = 1),
            fc_v = L.Linear(980,2)
        )

    def forward(self, x):
        h0 = F.max_pooling_2d(F.relu(self.conv0(x)), 2)
        h1 = F.max_pooling_2d(F.relu(self.conv1(h0)), 2)
        h2 = F.max_pooling_2d(F.relu(self.conv2(h1)), 2)
        h3 = F.max_pooling_2d(F.relu(self.conv3(h2)), 2)
        out_v = self.fc_v(h3)
        return out_v


def learn(x_train, t_train, test, test_answer):
    model = CNN()
    serializers.load_npz("test_model", model)
    optimizer = optimizers.SGD()
    optimizer.setup(model)

    n_epoch = 100
    batch_size = 4
    N = 30

    for epoch in range(0,n_epoch):
        sum_loss = 0
        sum_accuracy = 0
        perm = np.random.permutation(N)
        for i in range(0, len(x_train), batch_size):
            x = Variable(x_train[perm[i:i+batch_size]])
            t = Variable(t_train[perm[i:i+batch_size]])
            y = model.forward(x)
            model.zerograds()
            #loss = F.mean_squared_error(y, t)
            loss = F.softmax_cross_entropy(y, t)
            loss.backward()
            optimizer.update()
        print("epoch: {}".format(epoch))

    
    serializers.save_npz("test_model", model)
    tea = model.forward(test)
    print(tea)
    tea = np.argmax(tea.data, axis=1)
    print(tea)
    print(np.sum(tea == test_answer) / 10 * 100)

def main():
    x1,x2 = learn_data.execute()
    answer = np.array([])
    x_data = []
    test = []
    test_answer = np.array([])
    
    for i in range(0, 5):
        test.append(x1[i])
        test_answer = np.append( test_answer, int(0))
        test.append(x2[i])
        test_answer = np.append( test_answer, int(1))
        
    for i in range(5, len(x1)):
        answer = np.append(answer, int(0))
        x_data.append(x1[i])
        
    for i in range(5, len(x2)):
        answer = np.append(answer, int(1))
        x_data.append(x2[i])

    answer = answer.astype(np.int32)
    x_data = np.array(x_data, dtype=np.float32)
    test = np.array(test)
    learn(x_data, answer, test, test_answer)
main()

