#!/usr/bin/python3

import json
import re
import argparse

parser = argparse.ArgumentParser(description="Runtime parameters",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('filename', help='Source file', nargs='+')
parser.add_argument("-l", "--max_level", help="max display level", default=10000, type=int)
parser.add_argument('-p', '--pattern',   help='base model to use', default=None)

args = parser.parse_args()
config = vars(args)
q = {'dict': ['{', '}'], 'list': ['[', ']'], 'val': ["'", "'"]}


def human_bytes(size):
    for x in ['b', 'Kb', 'Mb', 'Gb', 'Tb']:
        if size < 1024.0:
            return "%5.1f %s" % (size, x)
        size /= 1024.0

    return size


def get_nested_size(item, storage, name, level=0):
    ll = 0

    if type(item) is dict:
        for key in dict.keys(item):
            ll += get_nested_size(item[key], storage, str(name) + '/' + str(key), level + 1)
            # Key Length
            ll += len(str(key))

        # Commas
        ll += len(item) - 1 if len(item) else 0
        # Brackets
        ll += 2
        storage.append({'len': ll, 'level': level, 'name': name, 'type': 'dict'})
    elif type(item) is list:
        for key, v in enumerate(item):
            ll += get_nested_size(v, storage, str(name) + '/' + str(key), level + 1)

        # Commas
        ll += len(item) - 1 if len(item) else 0
        # Brackets
        ll += 2
        storage.append({'len': ll, 'level': level, 'name': name, 'type': 'list'})
    else:
        ll = len(str(item))

        # Quotes
        if type(item) is not int and type(item) is not float:
            ll += 2

        storage.append({'len': ll, 'level': level, 'name': name, 'type': 'val'})

    return ll


with open(config['filename'][0], 'r', encoding='utf-8') as f:
    data = json.load(f)

storage = []
get_nested_size(data, storage, 'root')

for line in reversed(storage):
    if line['level'] < config['max_level'] and (not config['pattern'] or re.search(config['pattern'], line['name'])):
        hl = human_bytes(line['len'])
        print(hl + ' ' * (8 - len(hl)) + ' ' * (line['level'] * 4) + " - " + q[line['type']][0] + str(line['name']) + q[line['type']][1])
