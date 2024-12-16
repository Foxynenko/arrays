def replaceElements(arr):
    n = len(arr)
    if n == 1:
        return [-1]

    # Починаємо з останнього елемента
    max_right = -1

    for i in range(n - 1, -1, -1):
        current = arr[i]
        arr[i] = max_right
        max_right = max(max_right, current)

    return arr

# Приклади використання
arr1 = [17, 18, 5, 4, 6, 1]
print(replaceElements(arr1))  # Output: [18, 6, 6, 6, 1, -1]

arr2 = [400]
print(replaceElements(arr2))  # Output: [-1]
