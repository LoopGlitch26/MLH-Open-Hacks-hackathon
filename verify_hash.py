# from block import load_block
from hash_utils import validate_hash


def verify_chain(main_block):
    """
    It verifies all the hashes of the file.
    """
    # main_block = load_block()
    # print(main_block)

    for i in range(0, len(main_block)):
        if i != (len(main_block) - 1):
            next_block = main_block[i + 1]
            previous_hash = next_block['previous_hash']
            unique_num = next_block['id']

            # print(unique_num)

            block_to_be_checked = main_block[i]
            checked_hash = validate_hash(block_to_be_checked, unique_num)

            # print(checked_hash)
            # print(previous_hash)

            # print(str(checked_hash) == str(previous_hash))
            # break

            if str(checked_hash) == str(previous_hash):
                # print('Hash matched!')
                continue

            else:
                print('Error...')
                print(f'The block {block_to_be_checked} has been tampered :(' + '\n')
                print('Block ' + str(i) + ' hash: ' + checked_hash)
                print('Previous hash of ' + str(i + 1) + ': ' + previous_hash + '\n')
                return False

        print('All hash matched sucessfully!')
        return True


# verify_chain()
