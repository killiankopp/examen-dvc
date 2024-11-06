from src.config_manager import ConfigurationManager
from src.evaluation import ModelEvaluation

config = ConfigurationManager()
model_evaluate_config = config.get_model_evaluate_config()
evaluate = ModelEvaluation(config = model_evaluate_config)
evaluate.log_into_mlflow()
