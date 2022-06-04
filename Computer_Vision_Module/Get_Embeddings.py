import tensorflow as tf
global graph
from numpy import expand_dims

graph = tf.get_default_graph()


def get_embedding(model, face_pixels):
  '''
  GET EMBEDDINGS FOR ONLY ONE FACE
  '''
  print("Shape of image" ,face_pixels.shape )
  face_pixels = face_pixels.astype('float32') # scale pixel values
  mean, std = face_pixels.mean(), face_pixels.std() # stand