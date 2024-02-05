import os
from winequality import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from winequality.config.configuration import DataTransformationConfig


class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        df = pd.read_csv(self.config.data_dir)

        #splitting data in to train test sets
        train,test = train_test_split(df)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index =False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("splitted data in to training and test data")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)