from gendiff.formatters.bool_to_str import bool_to_str


def get_plain_formated_value(value):
    if isinstance(value, (dict, list, tuple, set)):
        value = "[complex value]"
    elif isinstance(value, str):
        value = f"'{value}'"
    value = bool_to_str(value)

    return value


def get_plain_formated_path(path):
    separator = '.'
    return separator.join(path)


def message_format(path, value, next_value):
    value = get_plain_formated_value(value)
    next_value = get_plain_formated_value(next_value)
    path = get_plain_formated_path(path)

    added = f"Property '{path}' was added with value: {value}"
    removed = f"Property '{path}' was removed"
    updated = f"Property '{path}' was updated. From {value} to {next_value}"

    return {'added': added, 'removed': removed, 'updated': updated}


def get_added(message):
    return message['added']


def get_removed(message):
    return message['removed']


def get_updated(message):
    return message['updated']


def plain(data):
    result = []

    def dict_to_str(data, start_path=[]):
        for key, value in data.items():
            orig_key = key[2:]
            path = start_path + [orig_key]
            messages = message_format(path, value, data.get(f"+ {orig_key}"))

            if key.startswith(('  ')) and isinstance(value, dict):
                dict_to_str(value, path)
            elif key.startswith(('- ')) and f"+ {orig_key}" in data:
                result.append(get_updated(messages))
            elif key.startswith(('- ')) and f"+ {orig_key}" not in data:
                result.append(get_removed(messages))
            elif key.startswith(('+ ')) and f"- {orig_key}" not in data:
                result.append(get_added(messages))

        return '\n'.join(result)

    return dict_to_str(data)
