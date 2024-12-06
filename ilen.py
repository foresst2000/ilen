def ilen(item = None) -> int:
    if item is None or len(item) == 0 or (item is not str and item is not list):
        # checks
        return 0
    
    length: int = -1

    for v in item:
        length += 1

    return length
