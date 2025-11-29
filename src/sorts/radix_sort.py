def radix_sort(a: list[int], base: int = 10) -> list[int]:
    if len(a) == 0:
        return []
    maxi_el = len(str(max(a)))
    for el in a:
        if el < 0:
            raise ValueError("Negative for radix sort\n Введите другое число, перезапустив программу")
        if int(el) != el:
            raise ValueError("Float for radix sort\n Введите другое число, перезапустив программу")

    for i in range(0, maxi_el):
        digit_place = [[] for el in range(base)]
        for el in a:
            digit = (el // base ** i) % base
            digit_place[digit].append(el)
        a = []
        for numb in digit_place:
            for el in numb:
                a.append(el)
    return a

