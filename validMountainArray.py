def validMountainArray(arr):
    n = len(arr)
    if n < 3:
        return False

    i = 0

    # Підйом вгору
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    # Перевірка, чи досягнуто вершини
    if i == 0 or i == n - 1:
        return False

    # Спуск вниз
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    # Перевірка, чи досягнуто кінця масиву
    return i == n - 1

# Приклади використання
arr1 = [2, 1]
print(validMountainArray(arr1))  # Output: False

arr2 = [3, 5, 5]
print(validMountainArray(arr2))  # Output: False

arr3 = [0, 3, 2, 1]
print(validMountainArray(arr3))  # Output: True
