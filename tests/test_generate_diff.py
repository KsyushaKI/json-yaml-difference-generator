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
    file_path1 = get_fixture_path('file1.json')
    file_path2 = get_fixture_path('file2.json')
    result_file_path = get_fixture_path('result.txt')
    correct_result_data = read(result_file_path)
    function_result = generate_diff(file_path1, file_path2)

    assert function_result == correct_result_data
