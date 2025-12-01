def heap_sort(a: list[int]) -> list[int]:
    build_max_heap(a)
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        max_heap(a, 0, i)
    return a
def build_max_heap(a):
    length = len(a)
    start = ((length - 1) - 1) // 2
    while start >= 0:
        max_heap(a, start, length)
        start = start - 1
def max_heap(a, index, size):
    l = 2 * index + 1
    r = 2 * index + 2
    if (l < size and a[l] > a[index]):
        largest = l
    else:
        largest = index
    if (r < size and a[r] > a[largest]):
        largest = r
    if (largest != index):
        a[largest], a[index] = a[index], a[largest]
        max_heap(a, largest, size)

