def q_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list) // 2]
    less_arr, equal_arr, big_arr =  [] ,