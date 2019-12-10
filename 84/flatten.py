def flatten(list_of_lists):
    return_list = []
    for item in list_of_lists:
        if isinstance(item, (list, tuple)):
            return_list += flatten(item)
        else:
            return_list.append(item)
    return return_list
