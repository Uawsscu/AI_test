import tensorflow as tf

v1 = tf.get_variable("v1", shape=[3], initializer = tf.zeros_initializer)
v2 = tf.get_variable("v2", shape=[5], initializer = tf.zeros_initializer)

f1 = v1.assign(v1+1)
f2 = v2.assign(v2+3)

saver = tf.train.Saver()

with tf.Session() as sess:

  tf.global_variables_initializer().run()
  print v1.eval()
  print v2.eval()
  f1.eval()
  f2.eval()

  save_path = saver.save(sess, "tmp/model.ckpt")
  print("Model saved in file: %s" % save_path)