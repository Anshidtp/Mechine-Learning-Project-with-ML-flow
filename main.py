from winequality import logger
from winequality.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from winequality.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from winequality.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from winequality.pipeline.stage04_model_trainer import ModelTrainingPipeline

STAGE_NAME = "Data_Ingestion_Stage"


if __name__ == '__main__':
    try:
        logger.info(f"{STAGE_NAME} started")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data_Validation_Stage"

if __name__=='__main__':
    try:
        logger.info(f"{STAGE_NAME} started")
        obj =DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Data_Transformation_Stage"

if __name__=='__main__':
    try:
        logger.info(f"{STAGE_NAME} started")
        obj =DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Trainer Stage"

if __name__=='__main__':
    try:
        logger.info(f"{STAGE_NAME} started")
        obj =ModelTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e


