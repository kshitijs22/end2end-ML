import sys
import os
import pickle

from src.exception import CustomException
from src.logger import logging

def save_object(filepath,object):
    try:
        dir_name=os.path.dirname(filepath)
        os.makedirs(dir_name,exist_ok=True)

        with open(filepath,'wb') as f:
            pickle.dump(object,f)
    except Exception as e:
        raise CustomException(e,sys)

