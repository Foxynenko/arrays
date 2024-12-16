def sortedSquares(nums):
    # Ініціалізація двох вказівників
    left, right = 0, len(nums) - 1
    result = [0] * len(nums)
    pos = len(nums) - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1
        pos -= 1

    return result

# Приклади використання
nums1 = [-4, -1, 0, 3, 10]
print(sortedSquares(nums1))  # Output: [0, 1, 9, 16, 100]

nums2 = [-7, -3, 2, 3, 11]
print(sortedSquares(nums2))  # Output: [4, 9, 9, 49, 121]
