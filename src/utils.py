import sys
import os
import pickle

from src.exception import CustomException
from src.logger import logging

from sklearn.metrics import r2_score

def save_object(filepath,object):
    try:
        dir_name=os.path.dirname(filepath)
        os.makedirs(dir_name,exist_ok=True)

        with open(filepath,'wb') as f:
            pickle.dump(object,f)
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report={}

        for i in range(len(list(models))):
            model=list(models.values())[i]

            model.fit(X_train,y_train)

            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)

            test_model_score=r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]]=test_model_score

        return report
    except Exception as e:
        raise CustomException(e,sys)


