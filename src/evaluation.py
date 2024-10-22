import logging
from pathlib import Path

import numpy as np
import pandas as pd
import mlflow
import mlflow.sklearn
import dagshub
import joblib
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from custom_logger import logger
from src.config_manager import ConfigurationManager
from src.entity import ModelEvaluationConfig
from src.common_utils import save_json

config = ConfigurationManager()
dagshub_config = config.get_dagshub_config()
dagshub.init(repo_owner = dagshub_config.repo_owner,
             repo_name = dagshub_config.repo_name,
             mlflow = dagshub_config.mlflow)


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        X_test = pd.read_csv(self.config.X_test_path)
        y_test = pd.read_csv(self.config.y_test_path)
        model = joblib.load(self.config.model_path)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        try:
            with mlflow.start_run():
                predicted_qualities = model.predict(X_test)

                (rmse, mae, r2) = self.eval_metrics(y_test, predicted_qualities)
                scores = {"rmse": rmse, "mae": mae, "r2": r2}
                save_json(path = Path(self.config.metric_file_name), data = scores)

                mlflow.log_params(self.config.all_params)

                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("mae", mae)
                mlflow.log_metric("r2", r2)

                mlflow.sklearn.log_model(
                    model,
                    "model",
                    registered_model_name="RandomForestRegressor"
                )
        except Exception as e:
            logger.error(e)
        raise