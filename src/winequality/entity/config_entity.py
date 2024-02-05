from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_URL : Path
    unzip_dir : Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    status_file: str
    schema : dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_dir: Path
    