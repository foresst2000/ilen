def slen(item = None) -> int:
    if item is None or len(item) == 0 or item is not str or item is not list:
        # checks
        return 0

    length: int = -1

    for v in item:
        # Object checking for none has already been passed
        length += 1

    return length
