def sortArrayByParity(nums):
    return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]

# Приклади використання
nums1 = [3, 1, 2, 4]
print(sortArrayByParity(nums1))  # Output: [2, 4, 3, 1] або інший прийнятний результат

nums2 = [0]
print(sortArrayByParity(nums2))  # Output: [0]
