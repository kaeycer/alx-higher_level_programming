def new_in_list(my_list, idx, element):

    counter = 0
    i = len(my_list)
    while counter < i:
        old_list[counter] = my_list[counter]
        counter += 1
    if (idx < 0) or (idx > len(my_list) - 1):
        return (my_list)
    else:
        # el = my_list
        old_list[idx] = element
        return (old_list)
