import json
import pickle

def save_block(block=None, filename=None):
    from block import main_block

    if filename is None:
        filename = 'output.block'

    with open(filename, mode='wb') as outfile:
        save_data = {
            'chain': main_block
        }
        outfile.write(pickle.dumps(save_data))