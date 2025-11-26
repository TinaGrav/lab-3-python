def bubble_sort(a: list[int]) -> list[int]:
    count_replacements = 1
    while count_replacements != 0:
        count_replacements = 0
        for element in range(len(a) - 1):
            if a[element] > a[element+1]:
                a[element], a[element+1] = a[element+1], a[element]
                count_replacements += 1
    return a