import tensorflow as tf
import numpy as np

class Model():
    def __init__(self, n_inputs, num_actions, n_hidden = 64):
        self.n_hidden = n_hidden

        self.weights = {
            'h1': tf.Variable(tf.random_normal([n_inputs, n_hidden])),
            'out': tf.Variable(tf.random_normal([n_hidden, num_actions]))
        }
        self.biases = {
            'h1': tf.Variable(tf.random_normal([n_hidden])),
            'out': tf.Variable(tf.random_normal([num_actions]))
        }

        self.x = tf.placeholder(tf.float32, [1, n_inputs])
        self.reward = tf.placeholder(tf.float32, [1])

        self.sess = tf.Session()
        self._build()



    def _build(self):
        self.lay = tf.add(tf.matmul(self.x, self.weights['h1']), self.biases['h1'])
        self.lay = tf.nn.relu(self.lay)

        self.lay = tf.add(tf.matmul(self.lay, self.weights['out']), self.biases['out'])
        self.lay = tf.nn.relu(self.lay)
        self.lay = tf.nn.softmax(self.lay)
        self.preds = tf.argmax(self.lay, 1)

        self.cost = tf.reduce_mean(1 - tf.square(self.reward - self.lay))
        self.optimizer = tf.train.AdamOptimizer(learning_rate=0.1).minimize(self.cost)

        init = tf.global_variables_initializer()
        self.sess.run(init)

    def train(self, x, reward):
        x = np.reshape(x, (1, 4))
        cost, _ = self.sess.run([self.cost, self.optimizer], feed_dict = {self.x : x,  self.reward: [reward]})
        print("cost: {}".format(cost))

    def pred(self, x):
        x = np.reshape(x, (1, 4))
        preds = self.sess.run([self.preds], feed_dict = {self.x : x})

        return preds[0][0]