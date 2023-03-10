from pathlib import Path
import json
import yaml


def get_path_to_file(file_path):
    path_to_file = Path(file_path)

    return path_to_file


def convert_data_to_python(file_path):
    file_path = file_path.lower()
    if file_path.endswith('.json'):
        return json.load(open(get_path_to_file(file_path)))
    elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
        return yaml.safe_load(open(get_path_to_file(file_path)))
