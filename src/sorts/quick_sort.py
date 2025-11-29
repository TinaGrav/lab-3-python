def quick_sort(a: list[int]) -> list[int]:
    if len(a) == 0:
        return a
    start_element = a[len(a) // 2]
    left_list = [el for el in a
                 if el < start_element]
    middle_list = [el for el in a
                   if el == start_element]
    right_list = [el for el in a
                  if el > start_element]
    return quick_sort(left_list) + middle_list + quick_sort(right_list)

