import tensorflow as tf
import numpy as np
 
import matplotlib.pyplot as plt

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

#data = np.genfromtxt("data.csv", delimiter=",") # read csv file (don't forget to download!)
#x_data= data[:,0]
#y_data= data[:,1]


#############################        
#print(x_data)
#print(y_data)
plt.plot(x_data, y_data, 'bx')
#plt.axis([0, 1, 0, 1])
plt.axis([0, 70, 0, 120])
plt.show()
#############################
 
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
#W1 = tf.Variable(tf.random_normal([200, 10], stddev=1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b
 
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
 
init = tf.initialize_all_variables()
 
# Launch the graph.
sess = tf.Session()
sess.run(init)
 
for step in xrange(201):
    sess.run(train)
    if step % 20 == 0:
        #test = sess.run(W)
        #print('W = '+ str(test[0]))
        print(step, sess.run(W), sess.run(b), sess.run(loss))

