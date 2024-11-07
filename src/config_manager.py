from src.config import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.common_utils import read_yaml, create_directories
from src.entity import (DataTransformationConfig, DataNormalizationConfig, ModelTrainerConfig, ModelEvaluationConfig,
                        DagshubConfig)


class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

    def get_dagshub_config(self) -> DagshubConfig:
        config = self.config.dagshub

        dagshub_config = DagshubConfig(
            repo_owner = config.repo_owner,
            repo_name = config.repo_name,
            mlflow = config.mlflow
        )

        return dagshub_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path
        )

        return data_transformation_config

    def get_data_normalization_config(self) -> DataNormalizationConfig:
        config = self.config.data_normalization

        create_directories([config.root_dir])

        data_normalization_config = DataNormalizationConfig(
            root_dir = config.root_dir
        )

        return data_normalization_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.RandomForestRegressor

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            X_train_path = config.X_train_path,
            y_train_path = config.y_train_path,
            n_estimators_grid = config.n_estimators_grid,
            max_depth_grid = config.max_depth_grid,
            best_model_name = config.best_model_name,
            model_name = config.model_name,
            criterion = params.criterion,
            min_samples_split = params.min_samples_split,
            min_samples_leaf = params.min_samples_leaf,
            max_features = params.max_features,
            random_state = params.random_state
        )

        return model_trainer_config

    def get_model_evaluate_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.RandomForestRegressor

        create_directories([config.root_dir])

        model_evaluate_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            X_test_path = config.X_test_path,
            y_test_path = config.y_test_path,
            model_path = config.model_path,
            metric_file_name = config.metric_file_name,
            mlflow_uri = config.mlflow_uri,
            all_params=params
        )

        return model_evaluate_config
