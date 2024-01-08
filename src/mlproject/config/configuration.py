
from src.mlproject.constants import *
from src.mlproject.utils.common import read_yaml, create_directories
from src.mlproject.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
      def __init__(
            self,
            config_filepath= CONFIG_FILE_PATH,
            params_filepath= PARAMS_FILE_PATH,
            schema_filepath= SCHEMA_FILE_PATH):
            
            self.config=read_yaml(config_filepath)
            self.params=read_yaml(params_filepath)
            self.schema=read_yaml(schema_filepath)

            create_directories([self.config.artifacts_root])

      def get_data_ingestion_config(self)-> DataIngestionConfig:
          initialize = self.config.data_ingestion

          create_directories([initialize.root_dir])

          data_ingestion_config = DataIngestionConfig(
                root_dir = initialize.root_dir,
                source_Url = initialize.source_Url,
                local_data_files = initialize.local_data_files,
                unzip_dir = initialize.unzip_dir
          )
         
          return data_ingestion_config

        