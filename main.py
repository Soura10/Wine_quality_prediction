from mlproject import logger
#from src.mlproject import logger
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlproject.pipeline.stage_02_data_validation import DataValidationTrainigPipeline
from src.mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline


STAGE_NAME= "Data Ingestion stage"
if __name__ == '__main__':
        try:
            logger.info(f">>>>stage {STAGE_NAME} started<<<<")
            obj=DataIngestionTrainingPipeline()
            obj.main()
            logger.info(f">>>stage {STAGE_NAME} Ccompleted<<<\n\nx=======x")
        except Exception as e:
            logger.exception(e)
            raise e    


STAGE_NAME= "Data Validation Stage"
try:
    logger.info(f">>>>stage {STAGE_NAME} started<<<<")
    obj=DataValidationTrainigPipeline()
    obj.main()
    logger.info(f">>>stage {STAGE_NAME} Ccompleted<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e    

STAGE_NAME= "Data Transformation stage"
try:
    logger.info(f">>>>stage {STAGE_NAME} started<<<<")
    obj=DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>stage {STAGE_NAME} Ccompleted<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e    
