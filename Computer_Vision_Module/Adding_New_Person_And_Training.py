import numpy as np
from numpy import load
from numpy import asarray
from numpy import savez_compressed
from .Variables import EMBEDDINGS_PATH,model,PATH_TO_ADDED_PERSON_FOLDER
from .Load_Dataset import load_dataset
from .Get_Embeddings import get_embedding
from .SVM_Classifier import svm_train

def add_person():
  '''
  Gets Images Embeddings of new person and concatenate them with the old Embeddings
  '''

  #