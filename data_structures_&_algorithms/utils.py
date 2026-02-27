def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            continue


def get_search_params():
    val = get_int("Enter a number to search: ")
    arr_size = get_int("Enter array size: ")
    return val, arr_size