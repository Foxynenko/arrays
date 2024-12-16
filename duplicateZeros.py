def duplicateZeros(arr):
    n = len(arr)
    zeros_to_duplicate = 0
    length = n - 1

    # Порахувати кількість нулів, які будуть дублюватися
    for i in range(n):
        if arr[i] == 0:
            if i + zeros_to_duplicate >= length:
                break
            zeros_to_duplicate += 1

    # Зворотній прохід для дублювання нулів
    for i in range(length - zeros_to_duplicate, -1, -1):
        if arr[i] == 0:
            if i + zeros_to_duplicate < n:
                arr[i + zeros_to_duplicate] = 0
            zeros_to_duplicate -= 1
            if i + zeros_to_duplicate < n:
                arr[i + zeros_to_duplicate] = 0
        else:
            if i + zeros_to_duplicate < n:
                arr[i + zeros_to_duplicate] = arr[i]

# Приклади використання
arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros(arr1)
print(arr1)  # Output: [1, 0, 0, 2, 3, 0, 0, 4]

arr2 = [1, 2, 3]
duplicateZeros(arr2)
print(arr2)  # Output: [1, 2, 3]
