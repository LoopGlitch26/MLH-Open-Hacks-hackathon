import json
import hashlib


def hash_string_256(string):
    # print(hashlib.sha256(string).hexdigest())
    return hashlib.sha256(string).hexdigest()


def hash_block(block):
    """Hashing a block and returns a string reprensentation of it.

    Arguments:
        :block: The block that should be hashed.
    """
    # Converting the "block" (which is dictionary) to 'string' and then encoding it to UTF-8.
    # return hash_string_256(json.dumps(block, sort_keys=True).encode())
    hash, unique_num = final_hash(block)
    return (hash, unique_num)


def final_hash(block):

    unique_num = 0
    guess_hash = hash_string_256(json.dumps(block, sort_keys=True).encode())
    while guess_hash[0:2] != '00':
        new_string = hash_string_256(json.dumps(
            block, sort_keys=True).encode()) + str(unique_num)
        guess_hash = hash_string_256(new_string.encode())
        # print(guess_hash)
        unique_num += 1
    return guess_hash, unique_num


def validate_hash(block, unique_num):
    """
    Generate the only vaild hash using unique 'number' and 'block'
    Arguments: 
        block: the block to be checked.
        unique_num: the unique id from the next hash
    """
    unique_num = unique_num - 1

    new_string = hash_string_256(json.dumps(
        block, sort_keys=True).encode()) + str(unique_num)
    guess_hash = hash_string_256(new_string.encode())
    # print(guess_hash)

    return guess_hash
