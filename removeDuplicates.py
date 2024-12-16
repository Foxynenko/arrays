def removeDuplicates(nums):
    if not nums:
        return 0

    # Ініціалізуємо вказівник для унікальних елементів
    unique_index = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]

    # Повертаємо кількість унікальних елементів
    return unique_index + 1

# Приклади використання
nums1 = [1, 1, 2]
k1 = removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 2, [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 5, [0, 1, 2, 3, 4]
