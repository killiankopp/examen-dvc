from src.config import CONFIG_FILE_PATH
from src.common_utils import read_yaml, create_directories
from src.entity import (DataTransformationConfig, DataNormalizationConfig, DataModelTrainerConfig)


class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path
        )

        return data_transformation_config

    def get_data_normalization_config(self) -> DataNormalizationConfig:
        config = self.config.data_normalization

        create_directories([config.root_dir])

        data_normalization_config = DataNormalizationConfig(
            root_dir = config.root_dir
        )

        return data_normalization_config

    def get_data_trainer_config(self) -> DataModelTrainerConfig:
        config = self.config.data_model_trainer

        create_directories([config.root_dir])

        data_model_trainer_config = DataModelTrainerConfig(
            root_dir = config.root_dir
        )

        return data_model_trainer_config
