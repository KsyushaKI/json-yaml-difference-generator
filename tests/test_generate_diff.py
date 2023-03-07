import os
from gendiff.generate_diff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_finding_different():
    jsone_path1 = get_fixture_path('file1.json')
    jsone_path2 = get_fixture_path('file2.json')
    yml_path1 = get_fixture_path('file1.yml')
    yml_path2 = get_fixture_path('file2.yml')

    correct_result_data = read(get_fixture_path('result.txt'))
    function_result_with_json = generate_diff(jsone_path1, jsone_path2)
    function_result_with_yml = generate_diff(yml_path1, yml_path2)

    assert function_result_with_json == correct_result_data
    assert function_result_with_yml == correct_result_data
