from gendiff.help_tools.convert_files_to_python import convert_data_to_python
from gendiff.help_tools.data_parser import get_diff
from gendiff.formatters.get_format import get_format


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1 = convert_data_to_python(file_path1)
    dict2 = convert_data_to_python(file_path2)
    diff = get_diff(dict1, dict2)

    return get_format(diff, format)
