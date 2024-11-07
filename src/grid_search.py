import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import pandas as pd

from custom_logger import logger
from src.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        X_train = pd.read_csv(self.config.X_train_path)
        y_train = pd.read_csv(self.config.y_train_path)

        rf = RandomForestRegressor(random_state=42)

        param_grid = {
            'n_estimators': self.config.n_estimators_grid,
            'max_depth': self.config.max_depth_grid
        }

        grid_search = GridSearchCV(
            estimator=rf,
            param_grid=param_grid,
            cv=5,
            scoring='r2',
            n_jobs=-1,
            verbose=2
        )

        grid_search.fit(X_train, y_train.values.ravel())

        joblib.dump(grid_search.best_params_, os.path.join(self.config.root_dir, self.config.best_model_name))

        print("Meilleurs paramètres :", grid_search.best_params_)
        print("Meilleur score (R^2) :", grid_search.best_score_)