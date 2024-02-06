from winequality import logger
from winequality.config.configuration import ConfigurationManager
from winequality.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config =ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()

STAGE_NAME = "Model Evaluation Stage"

if __name__=='__main__':
    try:
        logger.info(f"{STAGE_NAME} started")
        obj =ModelEvaluationPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e
    
