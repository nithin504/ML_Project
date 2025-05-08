import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
@dataclass
class DataIngesionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.Ingestion_config=DataIngesionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("enter the ingestion method or component")
        try:
            data=pd.read_csv("notebook\data\stud.csv")
            logging.info("read the dataset as datafream")   
            os.makedirs(os.path.dirname(self.Ingestion_config.train_data_path),exist_ok=True)
            data.to_csv(self.Ingestion_config.raw_data_path,index=False,header=True)
            logging.info("tain and test split initiated")
            train_set,test_set=train_test_split(data,test_size=0.2,random_state=42)
            train_set.to_csv(self.Ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.Ingestion_config.test_data_path,index=False,header=True)
    
            return(
                self.Ingestion_config.train_data_path,
                self.Ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
    


         
