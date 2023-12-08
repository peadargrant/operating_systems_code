#!/usr/bin/env python3

from argparse import ArgumentParser
import os.path

parser = ArgumentParser(description='check lab folder for required items')
args = parser.parse_args()

folders = [
    {
        "name": "week01",
        "files": []
    },
    {
        "name": "week02",
        "files": []
    },
    {
        "name": "week03",
        "files": []
    },
    {
        "name": "week04",
        "files": []
    },
    {
        "name": "week05",
        "files": []
    },
    {
        "name": "week06",
        "files": []
    },
    {
        "name": "week07",
        "files": []
    }
]

for folder in folders:
    print('checking for folder %s' % folder['name'])

    if not os.path.isdir(folder['name']):
        raise Exception('folder %s does not exist' % folder['name'])

    print('found')

    if 0 == len(os.listdir(folder['name'])):
        raise Exception('folder %s is empty' % folder['name'])

print("All required files found")
