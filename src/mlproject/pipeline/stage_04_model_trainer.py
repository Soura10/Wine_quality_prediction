from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.model_trainer import ModelTrainer
from mlproject import logger


STAGE_NAME="Model Trainer Stage"


class ModelTrainerTrainingPipeline:
    def __init__(self):
       pass
    
    def main(self):
       config= ConfigurationManager()
       model_trainer_config = config.get_model_trainer_config()
       model_trainer_config = ModelTrainer(config=model_trainer_config)
       model_trainer_config.tarin()


if __name__=="__main__":
    try:
         logger.info(f">>>>stage {STAGE_NAME} started<<<<")
         obj=ModelTrainerTrainingPipeline
         obj.main()
         logger.info(f">>>stage {STAGE_NAME} Ccompleted<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e    

  