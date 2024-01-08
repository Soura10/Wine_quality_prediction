from mlproject import logger
#from src.mlproject import logger
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

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