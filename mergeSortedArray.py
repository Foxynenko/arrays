def merge(nums1, m, nums2, n):
    # Ініціалізація трьох вказівників
    p1 = m - 1  # Останній індекс елемента в nums1
    p2 = n - 1  # Останній індекс елемента в nums2
    p = m + n - 1  # Останній індекс у nums1 для об'єднаного масиву

    # Проходимо у зворотному порядку
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

# Приклади використання
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]

nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]
