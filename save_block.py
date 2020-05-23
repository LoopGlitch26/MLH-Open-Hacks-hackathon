import json

def save_block(block=None, filename=None):
    from block import main_block

    if filename is None:
        filename = 'output.json'

    with open(filename, mode='w') as outfile:
        save_data = {
            'chain': main_block
        }
        json.dump(save_data, outfile)