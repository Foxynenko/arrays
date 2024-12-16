def findNumbers(nums):
    def countDigits(num):
        return len(str(num))
    
    even_count = 0
    for num in nums:
        if countDigits(num) % 2 == 0:
            even_count += 1
    
    return even_count

# Приклади використання
nums1 = [12, 345, 2, 6, 7896]
print(findNumbers(nums1))  # Output: 2

nums2 = [555, 901, 482, 1771]
print(findNumbers(nums2))  # Output: 1
