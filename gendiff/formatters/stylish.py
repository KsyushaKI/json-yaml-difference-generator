from gendiff.formatters.bool_to_str import bool_to_str
from gendiff.help_tools.data_parser import COMMON, ADD, REMOVE


diffes = (COMMON, ADD, REMOVE)


def get_full_str(predicate, key, value):
    return f'{predicate}{key}: {value}'


def get_key_str(predicate, key):
    return f'{predicate}{key}: ' + '{'


def get_end_str(predicate):
    return f'{predicate}' + '}'


def stylish(data, replacer=' ', spases_count=4):
    result = ['{']

    def dict_to_str(data, level):
        predicate = replacer * (spases_count * level - len(ADD))
        predicate2 = replacer * spases_count * level
        predicate3 = replacer * spases_count * (level - 1)
        for k, v in data.items():
            v = bool_to_str(v)
            if not isinstance(v, dict):
                if k.startswith(diffes):
                    result.append(get_full_str(predicate, k, v))
                else:
                    result.append(get_full_str(predicate2, k, v))
            elif isinstance(v, dict):
                if k.startswith(diffes):
                    result.append(get_key_str(predicate, k))
                else:
                    result.append(get_key_str(predicate2, k))
                dict_to_str(v, level + 1)
        result.append(get_end_str(predicate3))

        return '\n'.join(result)

    return dict_to_str(data, 1)
