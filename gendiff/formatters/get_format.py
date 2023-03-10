from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json_format


def get_format(diff, format):
    if format == 'stylish':
        return stylish(diff)
    elif format == 'plain':
        return plain(diff)
    elif format == 'json':
        return get_json_format(diff)
    else:
        error = """Formatter not found!
        Available formatters: 'stylish', 'plain', 'json'"""
        return error
