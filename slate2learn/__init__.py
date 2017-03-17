import json
import os
from pprint import pprint

from chariTech.settings import BASE_DIR


def load_and_parse(filepath):
    with open(filepath, 'r') as data_file:
        data = data_file.read().replace('\n', '')
        data = data.split('=')[1]
        data = data[1:]
        data = data[0:-1]
    return json.loads(data)


CONTENT = load_and_parse(os.path.join(BASE_DIR, 'slate2learn/data/json/content.json'))
EXPERIENCES = load_and_parse(os.path.join(BASE_DIR, 'slate2learn/data/json/experiences.json'))
TRANSACTIONS = load_and_parse(os.path.join(BASE_DIR, 'slate2learn/data/json/transactions.json'))
LEARNERS = load_and_parse(os.path.join(BASE_DIR, 'slate2learn/data/json/learners.json'))
MEMORIES = load_and_parse(os.path.join(BASE_DIR, 'slate2learn/data/json/memories.json'))