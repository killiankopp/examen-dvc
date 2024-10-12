import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from custom_logger import logger
from src.entity import DataNormalizationConfig


class DataNormalization:
    def __init__(self, config: DataNormalizationConfig):
        self.config = config

    def normalize(self):
        scaler = MinMaxScaler()

        X_train = pd.read_csv(os.path.join(self.config.root_dir, "X_train.csv"))
        X_test = pd.read_csv(os.path.join(self.config.root_dir, "X_test.csv"))

        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        X_train_scaled.to_csv(os.path.join(self.config.root_dir, "X_train_scaled.csv"), index=False)
        X_test_scaled.to_csv(os.path.join(self.config.root_dir, "X_test_scaled.csv"), index=False)

        logger.info("Normalized data")
        logger.info(f"X_train_scaled shape: {X_train_scaled.shape}")
        logger.info(f"X_test_scaled shape: {X_test_scaled.shape}")

        print(X_train_scaled.shape)
        print(X_test_scaled.shape)
