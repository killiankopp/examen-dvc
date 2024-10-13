from src.config_manager import ConfigurationManager
from src.transformation import DataTransformation

config = ConfigurationManager()
data_transformation_config = config.get_data_transformation_config()
data_transformation = DataTransformation(config = data_transformation_config)
data_transformation.train_test_splitting()