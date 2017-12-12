import tensorflow as tf    

input_data = [[0., 0.], [0., 1.], [1., 0.], [1., 1.]]  # XOR input
output_data = [[0.], [1.], [1.], [0.]]  # XOR output

n_input = tf.placeholder(tf.float32, shape=[None, 2], name="n_input")
n_output = tf.placeholder(tf.float32, shape=[None, 1], name="n_output")

# number of neurons in the hidden layer
hidden_nodes = 5


################
# hidden layer #
################

# hidden layer's bias neuron
b_hidden = tf.Variable(tf.random_normal([hidden_nodes]), name="hidden_bias")

# hidden layer's weight matrix initialized with a uniform distribution
W_hidden = tf.Variable(tf.random_normal([2, hidden_nodes]), name="hidden_weights")

# calc hidden layer's activation
hidden = tf.sigmoid(tf.matmul(n_input, W_hidden) + b_hidden)
#hidden = tf.matmul(n_input, W_hidden) + b_hidden

################
# output layer #
################

W_output = tf.Variable(tf.random_normal([hidden_nodes, 1]), name="output_weights")  # output layer's weight matrix
output = tf.sigmoid(tf.matmul(hidden, W_output))  # calc output layer's activation

############
# learning #
############
loss = tf.reduce_mean(tf.square(output - n_output))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)


####################
# initialize graph #
####################
#tf.global_variables_initializer
init = tf.global_variables_initializer()

sess = tf.Session()  
sess.run(init)  # initialize all variables  

#####################
# train the network #
#####################
for epoch in xrange(0, 2000):
    # run the training operation
    cvalues = sess.run([train, loss, W_hidden, b_hidden, W_output],
                       feed_dict={n_input: input_data, n_output: output_data})

    # print some debug stuff
    if epoch % 200 == 0:
        print("")
        print("step: %d" % epoch)
        print("loss: %f" % cvalues[1])
        
        # print("b_hidden: {}".format(cvalues[3]))
        # print("W_hidden: {}".format(cvalues[2]))
        # print("W_output: {}".format(cvalues[4]))


print("input: {} | output: {}".format(input_data[0], sess.run(output, feed_dict={n_input: [input_data[0]]})))
print("input: {} | output: {}".format(input_data[1], sess.run(output, feed_dict={n_input: [input_data[1]]})))
print("input: {} | output: {}".format(input_data[2], sess.run(output, feed_dict={n_input: [input_data[2]]})))
print("input: {} | output: {}".format(input_data[3], sess.run(output, feed_dict={n_input: [input_data[3]]})))

