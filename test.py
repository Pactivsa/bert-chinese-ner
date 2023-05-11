#测试tf是否可以使用gpu
import tensorflow as tf
print(tf.test.is_gpu_available())