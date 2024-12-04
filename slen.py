def slen(item = None) -> int:
    if item is None or len(item) == 0:
        # checks
        return 0

    if item is not str and item is not list:
        # check #2
        return 0
    
    length: int = -1

    for v in item:
        # Object checking for none has already been passed
        length += 1

    return length
