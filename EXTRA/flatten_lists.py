def flatten(listed):
    result = []
    for x in listed:
        result.extend(x)
    return result
flatten([[1, 2], [3, 4]])