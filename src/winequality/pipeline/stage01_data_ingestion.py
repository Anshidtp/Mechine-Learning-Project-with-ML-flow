from winequality.config.configuration import ConfigurationManager
from winequality.components.data_ingestion import DataIngestion
from winequality import logger

STAGE_NAME = "Data_Ingestion_Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f"{STAGE_NAME} stage started")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} stage completed")
    except Exception as e:
        logger.exception(e)
        raise e

