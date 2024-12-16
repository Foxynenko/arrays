def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

# Приклади використання
nums1 = [1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(nums1))  # Output: 3

nums2 = [1, 0, 1, 1, 0, 1]
print(findMaxConsecutiveOnes(nums2))  # Output: 2
