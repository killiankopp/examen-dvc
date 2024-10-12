from src.config import CONFIG_FILE_PATH, SCHEMA_FILE_PATH, PARAMS_FILE_PATH
from src.common_utils import read_yaml, create_directories
from src.entity import (DataTransformationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH):

            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)
            self.schema = read_yaml(schema_filepath)
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
          config = self.config.data_transformation

          create_directories([config.root_dir])

          data_transformation_config = DataTransformationConfig(
                root_dir = config.root_dir,
                data_path =  config.data_path,
          )

          return data_transformation_config