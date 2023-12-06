import os
from box.exceptions import BoxValueError
import yaml
from src.mlproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    '''
    read yaml file and returns

    Args:
         path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is emty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type             
    '''

    try:

        with open(path_to_yaml)as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        Raise ValueError("yaml file is emty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: ;ist, verbose=True):
    """create list of directories
    
    Args:
         path_to_directories (list) : list of path of directories
         ignore_log (bool,optional): ignore if multiple dirs is to be created. Defaults to false.
        """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


