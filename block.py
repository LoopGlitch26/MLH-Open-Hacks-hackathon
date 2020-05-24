from hash_utils import hash_block
from save_block import save_block
from verify_hash import verify_chain
# import json
import pickle

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'details': '',
    'id': 0
}

main_block = list()
main_block = [genesis_block]


def add_block(detail):
    global main_block
    previous_block = main_block[-1]
    previous_hash, unique_num = hash_block(previous_block)

    new_block = {
        'previous_hash': previous_hash,
        'index': len(main_block),
        'details': detail,
        'id': unique_num
    }
    main_block.append(new_block)
    # print(main_block)
    return main_block


def get_block():
    print(main_block)
    save_block(main_block)
    return main_block


def load_block(filename=None):
    """
    Returns main-block
    Arguments: filename
    """
    global main_block

    with open(filename, mode='rb') as file:
        # file_content = json.load(file)
        file_content = pickle.loads(file.read())
        main_block = file_content['chain']
        # print('loaded')
        # print(main_block)
        if verify_chain(main_block):
            return main_block
        else:
            print('Invalid chain...')
            return False


if __name__ == '__main__()':
    print('Hello')
    try:
        load_block()
    except Exception as e:
        print(e)
