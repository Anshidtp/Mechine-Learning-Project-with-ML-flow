from winequality.config.configuration import ConfigurationManager
from winequality.components.data_transformation import DataTransformation
from winequality import logger
from pathlib import Path


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation= DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()


STAGE_NAME = "Data_Transformation_Stage"

if __name__=='__main__':
    try:
        with open(Path("artifacts/data_validation/status.txt"), "r")as f:
            status = f.read().split(" ")[-1]
        
        if status == "True" :

            logger.info(f"{STAGE_NAME} started")
            obj =DataTransformationTrainingPipeline()
            obj.main()
            logger.info(f"{STAGE_NAME} completed")
        else:
            raise Exception("your data schema is not valid")
        
    except Exception as e:
        logger.exception(e)
        raise e



