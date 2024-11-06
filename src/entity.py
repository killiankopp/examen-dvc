from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DagshubConfig:
    repo_owner: str
    repo_name: str
    mlflow: bool


@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass(frozen = True)
class DataNormalizationConfig:
    root_dir: Path


@dataclass(frozen = True)
class ModelTrainerConfig:
    root_dir: Path
    X_train_path: Path
    y_train_path: Path
    n_estimators_grid: list
    max_depth_grid: list
    best_model_name: str
    model_name: str
    n_estimators: int
    max_depth: int
    criterion: str
    min_samples_split: int
    min_samples_leaf: int
    max_features: int
    random_state: int


@dataclass(frozen = True)
class ModelEvaluationConfig:
    root_dir: Path
    X_test_path: Path
    y_test_path: Path
    model_path: Path
    metric_file_name: Path
    all_params: dict
    metric_file_name: Path
    mlflow_uri: str
