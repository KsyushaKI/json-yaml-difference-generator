from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def get_format(diff, format):
    if format == 'stylish':
        return stylish(diff)
    elif format == 'plain':
        return plain(diff)
