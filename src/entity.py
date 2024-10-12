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
    max_depth: Optional[int] = 10
    n_estimators: Optional[int] = 100
    model_name: str = "rf"
