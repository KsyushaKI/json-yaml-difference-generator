def get_diff(dict1, dict2, common='  ', add='+ ', remove='- '):
    result = {}
    sorting = sorted(set(dict1) | set(dict2))
    for key in sorting:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result[f'{common}{key}'] = dict1[key]
            elif dict1[key] != dict2[key]:
                if type(dict1[key]) == dict and type(dict2[key]) == dict:
                    result[f'{common}{key}'] = get_diff(dict1[key], dict2[key])
                else:
                    result[f'{remove}{key}'] = dict1[key]
                    result[f'{add}{key}'] = dict2[key]
        elif key in dict1:
            result[f'{remove}{key}'] = dict1[key]
        elif key in dict2:
            result[f'{add}{key}'] = dict2[key]

    return result
