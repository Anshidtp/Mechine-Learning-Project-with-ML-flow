from winequality import logger
from winequality.config.configuration import ConfigurationManager
from winequality.components.model_trainer import ModelTrainer

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config  =config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


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