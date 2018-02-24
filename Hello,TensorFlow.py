#使用TensorFlow输出Hello,TensorFlow!
#Python3.5，TensorFlow1.5，Windows10
import tensorflow as tf
# hello = tf.constant（'Hello,TensorFlow!'）的情况下，hello是一个0维字符串tensor(张量)。
#因为在 TensorFlow 中, 数据并不会保存为 string,float等.。这些值都封装在 tensor 对象中。
#由tf.constant()返回的Tensor称为constant tensor(常数张量)，它的值不会改变。
hello = tf.constant('Hello, TensorFlow!')

# 使用tf.Session创建Session(会话)实例sess。 sess.run() 会运行上文定义的函数然后计算Tensot(张量)并返回结果。
sess = tf.Session()
# Run graph。
print (sess.run(hello).decode())
