from hash_utils import hash_block
from save_block import save_block
import json

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'details': ''
}

main_block = list()
main_block = [genesis_block]


def add_block(detail):
    global main_block
    previous_block = main_block[-1]
    previous_hash = hash_block(previous_block)

    new_block = {
        'previous_hash': previous_hash,
        'index': len(main_block),
        'details': detail
    }
    main_block.append(new_block)
    # print(main_block)
    return main_block


def get_block():
    print(main_block)
    save_block(main_block)
    return main_block


def load_block(filename=None):
    global main_block
    if filename is None:
        filename = 'output.json'

    with open(filename, mode='r') as file:
        file_content = json.load(file)
        main_block = file_content['chain']
        # print(main_block)
        return main_block


def save_block(block, filename=None):

    if filename is None:
        filename = 'output.json'

    with open(filename, mode='w+') as outfile:
        save_data = {
            'chain': block
        }
        json.dump(save_data, outfile)


if __name__ == '__main__()':
    print('Hello')
    try:
        load_block()
    except Exception as e:
        print(e)