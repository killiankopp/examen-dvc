import os
import joblib
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

from src.custom_logger import logger
from src.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        X_train = pd.read_csv(self.config.X_train_path)
        y_train = pd.read_csv(self.config.y_train_path)

        with open(os.path.join(self.config.root_dir, self.config.best_model_name), 'rb') as f:
            best_params = joblib.load(f)

        logger.info(f"n estimator: {best_params['n_estimators']}")
        logger.info(f"max depth: {best_params['max_depth']}")

        rf = RandomForestRegressor(
            n_estimators = best_params['n_estimators'],
            max_depth = best_params['max_depth'],
            criterion = self.config.criterion,
            max_features = self.config.max_features,
            min_samples_split = self.config.min_samples_split,
            min_samples_leaf = self.config.min_samples_leaf,
            random_state = self.config.random_state
        )

        rf.fit(X_train, y_train.values.ravel())

        joblib.dump(rf, os.path.join(self.config.root_dir, self.config.model_name))
