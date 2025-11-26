from sorts.bubble_sort import bubble_sort
def bucket_sort(a: list[float], buckets: int or None = None) -> list[float]:
    if len(a) == 0:
        return []
    if buckets == None:
        buckets = 4
    bucket_list = []
    for i in range(buckets):
        bucket_list.append([])
    max_el = max(a)
    for el in a:
        if el < 0:
            raise ValueError("Negative numbers for bucket sort")
        bucket_number = int(buckets * el / (max_el + 1))
        bucket_list[bucket_number].append(el)
    answer_list = []
    for bucket in bucket_list:
        bucket = bubble_sort(bucket)
        for number in bucket:
            answer_list.append(number)
    return answer_list
print(bucket_sort([1, 6, 0, 3, 8, 6, 5, 4], 3))