from winequality import logger
from winequality.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

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



