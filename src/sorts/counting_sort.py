def counting_sort(a: list[int]) -> list[int]:
    max_el = max(a)
    count_list = [0] * (max_el + 1)
    final_list = [0] * len(a)
    for el in a:
        if el < 0:
            raise ValueError("Negative for counting_sort\n Введите другое число, перезапустив программу")
        if int(el) != el:
            raise ValueError("Float for counting_sort\n Введите другое число, перезапустив программу")
        count_list[el] += 1
    for i in range(1, max_el + 1):
        count_list[i] += count_list[i - 1]
    for el in a:
        final_list[count_list[el] - 1] = el
        count_list[el] -= 1
    return final_list

