import os
import joblib
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from src.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        X_train = pd.read_csv(self.config.X_train_path)
        y_train = pd.read_csv(self.config.y_train_path)

        rf = RandomForestRegressor(
            n_estimators = self.config.n_estimators,
            max_depth = self.config.max_depth,
            random_state = 42
        )

        rf.fit(X_train, y_train.values.ravel())

        #name = f"rf_{self.config.n_estimators}_{self.config.max_depth}.pkl"

        joblib.dump(rf, os.path.join(self.config.root_dir, self.config.model_name))
