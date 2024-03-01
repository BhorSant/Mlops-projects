import os
from pathlib import Path
list_of_files = {
    ".github/workflows/gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/model_transformation.py",
    "src/components/model_training.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requrements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "requirements/experiments.ipynb"
}

for filename in list_of_files:
    filename = Path(filename)
    filedir,filename = os.path.split(filename)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(f"Creating directory {filedir} for file: {filename}")
        # logging.info(f"Creating directory {filedir} for file: {filename}")
    if not os.path.exists(filename) or (os.path.getsize(filename) == 0):
        with open(filename,"w") as f:
            pass