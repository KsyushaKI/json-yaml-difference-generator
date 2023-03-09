#!/usr/bin/env python3

from gendiff.args_parser import parser_arg
from gendiff.generate_diff import generate_diff


def main():
    file_path1, file_path2, format = parser_arg()
    print(generate_diff(file_path1, file_path2, format))


if __name__ == '__main__':
    main()
