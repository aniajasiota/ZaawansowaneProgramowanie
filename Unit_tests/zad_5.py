def flatten_list(nested_list: list) -> list:
    flist = []
    for i in nested_list:
        if type(i) == list:
            flist.extend(flatten_list(i))
        else:
            flist.append(i)

    return flist