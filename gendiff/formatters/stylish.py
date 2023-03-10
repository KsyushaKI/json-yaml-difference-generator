from gendiff.formatters.bool_to_str import bool_to_str


def stylish(data, replacer=' ', spases_count=4):
    result = ['{']

    def dict_to_str(data, level):
        predicate = replacer * (spases_count * level - 2)
        predicate2 = replacer * spases_count * level
        predicate3 = replacer * spases_count * (level - 1)
        for k, v in data.items():
            v = bool_to_str(v)
            if not isinstance(v, dict):
                if k.startswith(('+ ', '- ', '  ')):
                    result.append(f'{predicate}{k}: {v}')
                else:
                    result.append(f'{predicate2}{k}: {v}')
            elif isinstance(v, dict):
                if k.startswith(('+ ', '- ', '  ')):
                    result.append(f'{predicate}{k}: ' + '{')
                else:
                    result.append(f'{predicate2}{k}: ' + '{')
                dict_to_str(v, level + 1)
        result.append(f'{predicate3}' + '}')

        return '\n'.join(result)

    return dict_to_str(data, 1)
