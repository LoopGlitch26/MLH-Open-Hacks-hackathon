from hash_utils import hash_block

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'type': ''
}

main_block = [genesis_block]


def add_block(e_type):
    previous_block = main_block[-1]
    previous_hash = hash_block(previous_block)

    new_block = {
        'previous_hash': previous_hash,
        'index': len(main_block),
        'type': str(e_type).lower()
    }
    main_block.append(new_block)
    # print(main_block)


def get_block():
    print(main_block)
    return main_block
