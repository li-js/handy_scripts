# tensorflow_allow_growth
import tensorflow as tf
import keras.backend as K
tfconfig = tf.ConfigProto(allow_soft_placement=True)
tfconfig.gpu_options.allow_growth=True
sess = tf.Session(config=tfconfig)
K.set_session(sess)



# TF initialize only uninitialized_variables
uninitialized_var_names = sess.run(tf.report_uninitialized_variables())
sess.run(tf.variables_initializer([v for v in tf.global_variables() if v.name.split(':')[0] in uninitialized_var_names]))
