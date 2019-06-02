import tensorflow as tf

class Model():
    def __init__(self, n_inputs, num_actions, n_hidden = 16):
        self.n_hidden = n_hidden

        self.weights = {
            'out': tf.Variable(tf.random_normal(n_inputs, num_actions))
        }
        self.biases = {
            'out': tf.Variable(tf.random_normal(num_actions))
        }

        self.x = tf.placeholder(tf.float32, n_inputs)
        self.reward = tf.placeholder(tf.float32, 1)

        self.sess = tf.Session()
        self._build()



    def _build(self):
        self.lay = tf.add(tf.matmul(self.x, self.weights['out']), self.biases['out'])
        self.lay = tf.nn.relu(self.lay)
        self.lay = tf.nn.softmax(self.lay)

        self.cost = tf.reduce_mean(self.reward)
        self.optimizer = tf.train.AdamOptimizer(learning_rate=0.01).minimize(cost)

        init = tf.global_variables_initializer()
        self.sess.run(init)

    def train(self, reward):
        cost, _ = self.sess.run([self.cost, self.optimizer], feed_dict = {self.reward: reward})
        print("cost: {}".format(cost))

    def pred(self, x):
        preds = self.sess.run([self.lay], feed_dict = {self.x : x})

        return preds