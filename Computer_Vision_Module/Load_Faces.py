import os
import numpy as np
from os import listdir
from numpy import asarray
from numpy import load


from .Extract_Faces import extract_face


# load images and extract faces for all images in a directory
def load_faces(directory):
  '''
  THIS FUNCTION TAKES DIRECTORY OF (ONE) PERSON IMAGES AS INPUT
  OUTPUTS A FAC