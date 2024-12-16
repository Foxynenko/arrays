def checkIfExist(arr):
    seen = set()

    for num in arr:
        if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)

    return False

# Приклади використання
arr1 = [10, 2, 5, 3]
print(checkIfExist(arr1))  # Output: True

arr2 = [3, 1, 7, 11]
print(checkIfExist(arr2))  # Output: False
