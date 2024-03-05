import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from src.utils.utils import save_object,evaluate_model

from sklearn.linear_model import LinearRegression, Ridge,Lasso,ElasticNet

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def  __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    def initiate_data_training(self,train_array,test_array):
        try:
            logging.info("Splitting Dependent and Independent variable from train and test data")
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models={
                "LInearRegression":LinearRegression(),
                "Lasso":Lasso(),
                "Ridge":Ridge(),
                "Elasticnet":ElasticNet()
            }

            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print("\n===================================================================")
            logging.info(f"Model Report : {model_report}")

            # TO get best model score from directory
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            print(f"Best Model FOund, Model Name : {best_model_name}, R2_score : {best_model_score}")
            print("\n==================================================")
            logging.info(f"Best Model Found, Model Name : {best_model_name}, R2_score : {best_model_score}")

            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=best_model
            )
          

        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise customexception(e,sys)


