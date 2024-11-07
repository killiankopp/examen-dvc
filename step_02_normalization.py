from src.config_manager import ConfigurationManager
from src.normalisation import DataNormalization

config = ConfigurationManager()
data_normalization_config = config.get_data_normalization_config()
data_transformation = DataNormalization(config = data_normalization_config)
data_transformation.normalize()