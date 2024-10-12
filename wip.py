from src.config_manager import ConfigurationManager
from src.training import ModelTrainer

config = ConfigurationManager()
data_model_trainer_config = config.get_model_trainer_config()
data_transformation = ModelTrainer(config = data_model_trainer_config)
data_transformation.train()