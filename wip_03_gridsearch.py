from src.config_manager import ConfigurationManager
from src.grid_search import ModelTrainer

config = ConfigurationManager()
model_trainer_config = config.get_model_trainer_config()
trainer = ModelTrainer(config = model_trainer_config)
trainer.train()