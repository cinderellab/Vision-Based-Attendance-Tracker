import os
import mtcnn
from mtcnn.mtcnn import MTCNN

detector = MTCNN() # Creating instance from the class MTCNN

# EMBEDDINGS PATH
EMBEDDINGS_PATH = os.getcwd() 

# EMPLOYEES PATH
EMPLOYEES_NAMES = os.getcwd()

# SVM Model Path
SVM_MODEL_PATH = os.getcwd()


# Create Folders/Classes under photos dir in your Django Project
TRAINING_IMAGES_PATH = os.getcwd() + '\\..\\media\\photos' 



# Path of facenet_keras.h5 file
PATH_TO_FACENET_MODEL = os.getcwd()
FACENET_MODEL = PATH_TO_FACENET_MODEL + '\\facenet_keras.h5'


if o