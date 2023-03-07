import json
import yaml


def convert_json_yaml_to_python(file_path):
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
        return yaml.load(open(file_path), yaml.SafeLoader)


def find_diff(dict1, dict2):
    dict3 = {}
    for elem in sorted(dict1 | dict2):
        if elem in dict1 and elem in dict2:
            if dict1[elem] == dict2[elem]:
                dict3[f'  {elem}'] = dict1[elem]
            elif dict1[elem] != dict2[elem]:
                dict3[f'- {elem}'] = dict1[elem]
                dict3[f'+ {elem}'] = dict2[elem]
        elif elem in dict1:
            dict3[f'- {elem}'] = dict1[elem]
        elif elem in dict2:
            dict3[f'+ {elem}'] = dict2[elem]

    return dict3


def python_boolean_to_json_yaml_bolean(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    else:
        return value


def stringify(value, replacer=' ', spases_count=2):
    predicate = replacer * spases_count
    dict_ = ['{']

    def dict_to_str(value, level):
        for k, v in value.items():
            v = python_boolean_to_json_yaml_bolean(v)
            if not isinstance(v, dict):
                dict_.append(f'{predicate * level}{k}: {v}')
            elif isinstance(v, dict):
                dict_.append(f'{predicate * level}{k}: ' + '{')
                dict_to_str(v, level + 1)
        dict_.append(f'{predicate * (level - 1)}' + '}')

        return '\n'.join(dict_)

    return dict_to_str(value, 1)


def generate_diff(file_path1, file_path2):
    dict1 = convert_json_yaml_to_python(file_path1)
    dict2 = convert_json_yaml_to_python(file_path2)
    dict3 = find_diff(dict1, dict2)

    return stringify(dict3)
