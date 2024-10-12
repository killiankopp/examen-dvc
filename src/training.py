import os
import joblib
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from src.entity import DataModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: DataModelTrainerConfig):
        self.config = config

    def train(self):
        X_train = pd.read_csv(os.path.join(self.config.root_dir, "X_train_scaled.csv"))
        y_train = pd.read_csv(os.path.join(self.config.root_dir, "y_train.csv"))

        rf = RandomForestRegressor(
            n_estimators = self.config.n_estimators,
            max_depth = self.config.max_depth,
            random_state = 42
        )

        rf.fit(X_train, y_train.values)

        joblib.dump(rf, os.path.join(self.config.root_dir, self.config.model_name))
