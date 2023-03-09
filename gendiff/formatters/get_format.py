from gendiff.formatters.stylish import stylish


def get_format(diff, format):
    if format == 'stylish':
        return stylish(diff)
