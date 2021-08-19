def bubble_sort(list):
    last_element_index = len(list) - 1
    for pass_no in range(last_element_index, 0, -1):
        for idx in range(pass_no):
            if list[idx] > list[idx + 1]:
                list[idx], list[idx + 1] = list[idx + 1], list[idx]
    return list

list = [25, 21, 22, 24, 23, 27, 26]

print(bubble_sort(list))