import json


def get_dict_from_json(file_path):
    '''
    Works with both absolute and relative paths
    '''
    data = json.load(open(file_path))
    return data


def jsonify_repr(value):
    '''
    Converts Python value to JSON value representation
    '''
    if value == True:
        return 'true'
    elif value == False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def compare_data(data_1, data_2):
    '''
    Compares two dictionaries.
    Returns a dictionary with all keys and their status
    '''

    keys = data_1.keys() | data_2.keys()
    diff = {}

    for key in keys:
        if key not in data_1:
            diff[key] = 'added'
        elif key not in data_2:
            diff[key] = 'removed'
        elif data_1[key] == data_2[key]:
            diff[key] = 'unchanged'
        else:
            diff[key] = 'changed'
    return diff


def generate_diff(file_1, file_2):
    '''
    Generate JSON-like string that displays 
    difference between two JSON files.
    A sign before each key-value pair shows 
    how the file object was modified:
    deleted ('-'), added ('+'), unchanged (no sign). 

    {
        - follow: false
          host: "hexlet.io"
        - proxy: 123.234.53.22
        - timeout: 50
        + timeout: 20
        + verbose: true
    }
    '''

    data_1 = get_dict_from_json(file_1)
    data_2 = get_dict_from_json(file_2)

    diff = compare_data(data_1, data_2)
    
    flat_diff = []

    for obj, status in sorted(diff.items()):
        if status == 'removed':
            flat_diff.append(f'    - {obj}: {jsonify_repr(data_1.get(obj))}\n')
        elif status == 'added':
            flat_diff.append(f'    + {obj}: {jsonify_repr(data_2.get(obj))}\n')
        elif status == 'changed':
            flat_diff.append(f'    - {obj}: {jsonify_repr(data_1.get(obj))}\n')
            flat_diff.append(f'    + {obj}: {jsonify_repr(data_2.get(obj))}\n')
        else:
            flat_diff.append(f'      {obj}: {jsonify_repr(data_2.get(obj))}\n')

    return "{     " + "\n" + ''.join(flat_diff) + "}"
