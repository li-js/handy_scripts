import tensorflow as tf
import keras.backend as K
tfconfig = tf.ConfigProto(allow_soft_placement=True)
tfconfig.gpu_options.allow_growth=True
sess = tf.Session(config=tfconfig)
K.set_session(sess)
