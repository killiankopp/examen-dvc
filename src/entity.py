from dataclasses import dataclass
from pathlib import Path
from typing import Optional


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
    data_path: Path
    n_estimators: int
    max_depth: int
    model_name: str
