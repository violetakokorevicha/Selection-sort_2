def arr_sort(lst: list) -> list:
    changes_count = 0
    current_index = 0
    while True:
        if not changes_count > 0 and current_index + 1 == len(lst):
            break
           
        if current_index + 1 == len(lst) and changes_count > 0:
            changes_count, current_index = 0, 0
           
        if lst[current_index + 1] < lst[current_index]:
            temp = lst[current_index]
            lst[current_index] = lst[current_index + 1]
            lst[current_index + 1] = temp
            changes_count += 1
        current_index += 1
    return lst