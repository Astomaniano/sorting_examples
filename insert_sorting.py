# Сортировка вставками работает путем последовательного перемещения элементов массива,
# вставляя каждый элемент на его правильное место в уже отсортированной части массива.


def insert_sort(arr):
    for i in range (1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


a = [-3, 5, 0, -8, 1, 10]
print(insert_sort(a))