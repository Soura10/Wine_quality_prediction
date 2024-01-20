import os
from src.mlproject import logger
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib
from src.mlproject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config
        

    def tarin(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)    


        train_X = train_data.drop([self.config.target_cloumn],axis=1)
        test_X = test_data.drop([self.config.target_cloumn],axis=1)
        train_y = train_data[[self.config.target_cloumn]]
        test_y = test_data[[self.config.target_cloumn]]

        lr=ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_X,train_y)

        joblib.dump(lr,os.path.join(self.config.root_dir, self.config.model_name))

