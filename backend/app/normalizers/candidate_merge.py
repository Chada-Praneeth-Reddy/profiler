def choose_first(*values):
    for value in values:
        if value:
            return value

    return None