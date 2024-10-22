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
    n_estimators: int
    max_depth: int
    model_name: str


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
